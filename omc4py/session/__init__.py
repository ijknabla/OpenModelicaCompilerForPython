
import arpeggio  # type: ignore
import numpy
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import typing
import uuid
import warnings
import zmq  # type: ignore
from . import (
    exception,
    parser,
    string,
    visitor,
)


StrOrPathLike = typing.Union[str, os.PathLike]


def resolve_command(
    command: StrOrPathLike,
) -> Path:
    executable = shutil.which(command)
    if executable is None:
        raise FileNotFoundError(
            f"Can't find executable of {command}"
        )

    return Path(executable).resolve()


def find_openmodelica_zmq_port_filepath(
    suffix: typing.Optional[str]
) -> Path:
    temp_dir = Path(tempfile.gettempdir())

    pattern_of_name = "openmodelica*.port"
    if suffix is not None:
        pattern_of_name += f".{suffix}"

    candidates = tuple(temp_dir.glob(pattern_of_name))

    if not candidates:
        raise ValueError(
            f"Can't find openmodelica port file "
            f"at {temp_dir}"
        )
    elif len(candidates) >= 2:
        raise ValueError(
            f"Ambiguous openmodelica port file {candidates}"
            f"at {temp_dir}"
        )

    return candidates[0]


omc_error_pattern = re.compile(
    r"\[(?P<info>[^]]*)\]\s+(?P<kind>\w+):\s+(?P<message>.*)"
)


class InteractiveOMC(
    typing.NamedTuple
):
    socket: zmq.Socket
    process: subprocess.Popen

    @classmethod
    def open(
        cls,
        omc_command: typing.Optional[StrOrPathLike] = None,
    ) -> "InteractiveOMC":
        if omc_command is None:
            omc_command = "omc"

        suffix = str(uuid.uuid4())

        socket = zmq.Context().socket(
            # pylint: disable=no-member
            zmq.REQ
        )

        process = subprocess.Popen(
            [
                resolve_command(omc_command),
                "--interactive=zmq", f"-z={suffix}"
            ],
            universal_newlines=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
        )

        self = cls(
            socket=socket,
            process=process,
        )

        try:
            self.__connect_socket(suffix)
        except Exception:
            self.close()
            raise

        return self

    def __connect_socket(
        self,
        suffix: str
    ):
        process_stdout: typing.IO
        if self.process.stdout is None:
            ValueError(
                "Ensure that subprocee.Popen(stdout=subprocess.PIPE)"
            )
        else:
            process_stdout = self.process.stdout

        process_stdout.readline()

        port_filepath = find_openmodelica_zmq_port_filepath(suffix)

        try:
            self.socket.connect(port_filepath.read_text())
        finally:
            try:
                port_filepath.unlink()
            except FileNotFoundError:
                pass

    def close(
        self
    ) -> None:
        self.socket.close()
        self.process.terminate()

    def __enter__(
        self
    ):
        return self

    def __exit__(
        self,
        exc_type,
        exc_value,
        traceback,
    ):
        self.close()
        return False

    def evaluate(
        self,
        expression: str
    ) -> str:
        self.socket.send_string(expression)
        return self.socket.recv_string()

    def find_error(
        self
    ) -> typing.Optional[exception.OMCException]:
        error_message = string.unquote_modelica_string(
            self.evaluate("getErrorString()").rstrip()
        )
        if not error_message or error_message.isspace():
            return None

        matched = omc_error_pattern.match(
            error_message
        )
        if not matched:
            raise exception.OMCRuntimeError(
                f"Unexpected error message format: {error_message!r}"
            )
        # info = matched.group("info")
        kind = matched.group("kind")
        # message = matched.group("message")

        if kind == "Error":
            return exception.OMCError(error_message)
        elif kind == "Warning":
            return exception.OMCWarning(error_message)
        else:
            raise NotImplementedError(
                "Unexpected omc error kind: {kind!r}"
            )


def parse_omc_value(
    literal: str
):
    return arpeggio.visit_parse_tree(
        parser.omc_value_parser.parse(literal),
        visitor.OMCValueVisitor()
    )


class OMCSessionBase(
):
    _omc: InteractiveOMC

    def __init__(
        self,
        omc: InteractiveOMC
    ):
        self._omc = omc

    def __enter__(
        self,
    ):
        return self

    def __exit__(
        self,
        exc_type,
        exc_value,
        traceback,
    ):
        OMCSession__close(self)
        return False


def OMCSession__open(
    OMCSessionType: typing.Type[OMCSessionBase],
    omc_command: typing.Optional[StrOrPathLike] = None,
) -> OMCSessionBase:
    omc = InteractiveOMC.open(
        omc_command=omc_command,
    )
    return OMCSessionType(omc)


def OMCSession__close(
    self: OMCSessionBase
):
    self._omc.close()


PositionalArguments = typing.List[typing.Any]
KeywordArguments = typing.Dict[str, typing.Any]


def OMCSession__call(
    self: OMCSessionBase,
    funcName: str,
    *,
    args: typing.Optional[PositionalArguments] = None,
    kwrds: typing.Optional[KeywordArguments] = None,
) -> typing.Any:
    argument_literals: typing.List[str] = []
    if args is not None:
        for arg in args:
            argument_literals.append(
                string.to_omc_literal(arg)
            )
    if kwrds is not None:
        for ident, value in kwrds.items():
            if value is None:
                continue
            value_literal = string.to_omc_literal(
                value
            )
            argument_literals.append(
                f"{ident}={value_literal}"
            )

    arguments_literal = ", ".join(argument_literals)

    result_literal = self._omc.evaluate(
        f"{funcName}({arguments_literal})"
    )

    error = self._omc.find_error()

    if error is not None:
        if isinstance(error, Warning):
            warnings.warn(error)
        else:
            raise error

    return parse_omc_value(result_literal)


def check_scalar_value(
    class_or_tuple: typing.Union[typing.Type, typing.Tuple[typing.Type, ...]],
    optional: bool,
    name: str,
    value: typing.Any,
) -> typing.Any:
    if value is None:
        if optional:
            return None
        else:
            raise TypeError(
                f"{name} must be {class_or_tuple}, got None"
            )

    if isinstance(value, class_or_tuple):
        return value
    else:
        raise TypeError(
            f"{name} must be {class_or_tuple}"
            + " or None" if optional else ""
            + f", got {value!r}: {type(value).__name__}"
        )


def cast_scalar_value(
    class_: typing.Type,
    optional: bool,
    name: str,
    value: typing.Any,
) -> typing.Any:
    if value is None and optional:
        return None

    return class_(value)


def cast_array_value(
    class_: typing.Type,
    shape,
    optional: bool,
    name: str,
    value: typing.Any,
) -> typing.Any:
    if value is None and optional:
        return None

    arr = numpy.array(
        value,
        dtype=class_
    )
    if arr.dtype == numpy.object_:
        arr = numpy.vectorize(class_, otypes=[numpy.object_])(arr)

    assert(len(shape) == arr.ndim)
    return arr
