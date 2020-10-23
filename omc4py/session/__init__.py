
import arpeggio  # type: ignore
import atexit
import numpy
import os
import logging
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import typing
import typing_extensions
import uuid
import warnings
import zmq  # type: ignore

from . import (
    exception,
    parser,
    visitor,
)

from omc4py import string


logger = logging.getLogger(__name__)


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
    r"(\[(?P<info>[^]]*)\]\s+)?(?P<kind>\w+):\s+(?P<message>.*)"
)


class InteractiveOMC(
):
    __slots__ = (
        "__socket",
        "__process",
    )

    __instances: typing_extensions.Final[typing.Set["InteractiveOMC"]] \
        = set()

    __socket: zmq.Socket
    __process: subprocess.Popen

    def __new__(
        cls,
        socket: zmq.Socket,
        process: subprocess.Popen,
    ):
        self = super().__new__(cls)
        self.__socket = socket
        self.__process = process

        self.__instances.add(self)

        return self

    @property
    def socket(self) -> zmq.Socket: return self.__socket

    @property
    def process(self) -> subprocess.Popen: return self.__process

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

        command = [
            str(resolve_command(omc_command)),
            "--interactive=zmq", f"-z={suffix}",
        ]

        process = subprocess.Popen(
            command,
            universal_newlines=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
        )

        logger.info(
            "(pid={pid}) Start omc :: {scommand}".format(
                pid=process.pid,
                scommand=" ".join(command))
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

        logger.info(
            f"(pid={self.process.pid}) Find zmq port file at {port_filepath}"
        )

        try:
            port = port_filepath.read_text()
            self.socket.connect(port)
            logger.info(
                f"(pid={self.process.pid}) Connect zmq sokcet via {port}"
            )
        finally:
            try:
                port_filepath.unlink()
                logger.info(
                    f"(pid={self.process.pid}) Remove zmq port file at {port_filepath}"
                )
            except FileNotFoundError:
                pass

    def close(
        self,
    ) -> None:
        if self in self.__instances:
            self.socket.close()
            logger.info(
                f"(pid={self.process.pid}) Close zmq sokcet"
            )
            self.process.terminate()
            logger.info(
                f"(pid={self.process.pid}) Stop omc"
            )
            self.__instances.remove(self)

    @classmethod
    def close_all(
        cls,
    ) -> None:
        for self in cls.__instances.copy():
            self.close()

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
        logger.debug(
            f"(pid={self.process.pid}) >>> {expression}"
        )
        self.socket.send_string(expression)
        result = self.socket.recv_string()
        logger.debug(
            f"(pid={self.process.pid}) {result}"
        )
        return result

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
        else:
            return exception.OMCWarning(error_message)


atexit.register(InteractiveOMC.close_all)


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
    parse: bool = True,
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

    if parse:
        return parse_omc_value(result_literal)
    else:
        return result_literal


def cast_scalar_value(
    name: str,
    value: typing.Any,
    class_: typing.Type,
    class_restrictions: typing.Tuple[typing.Type, ...],
) -> typing.Any:
    if class_restrictions:
        if not isinstance(value, class_restrictions):
            raise TypeError(
                f"{name!r} must be an instance of {class_restrictions}"
                f", got {value!r}: {type(value)!r}"
            )
    return class_(value)


def sizes_to_str(
    sizes: typing.Tuple[typing.Optional[int], ...]
) -> str:
    return (
        "{"
        + ", ".join(
            str(size) if size is not None else ":"
            for size in sizes
        )
        + "}"
    )


def cast_array_value(
    name: str,
    value: typing.Any,
    class_: typing.Type,
    class_restrictions: typing.Tuple[typing.Type, ...],
    sizes: typing.Tuple[typing.Optional[int], ...],
) -> numpy.ndarray:
    object_array = numpy.array(value, dtype=object)

    same_n_dimensions = (len(sizes) == object_array.ndim)
    dimensions_are_correct = [
        True if expected is None else expected == actual
        for expected, actual in zip(sizes, object_array.shape)
    ]

    if not(same_n_dimensions and all(dimensions_are_correct)):
        raise ValueError(
            f"Shape of the array must be {sizes_to_str(sizes)}, "
            f"got {sizes_to_str(object_array.shape)}"
        )

    if class_restrictions:
        isinstance_vectorized = numpy.vectorize(
            lambda cls: isinstance(cls, class_restrictions),
            otypes=[numpy.dtype(bool)],
        )
        isinstance_mask = isinstance_vectorized(
            object_array
        )
        if not numpy.all(isinstance_mask):
            raise TypeError(
                f"All items of the array {name!r} "
                f"must be instances of {class_restrictions}"
            )

    class_vectorized = numpy.vectorize(
        class_, otypes=[numpy.dtype(class_)])
    return class_vectorized(object_array)


def cast_value(
    name: str,
    value: typing.Any,
    optional: bool,
    class_: typing.Type,
    class_restrictions: typing.Tuple[typing.Type, ...],
    sizes: typing.Tuple[typing.Optional[int], ...],
) -> typing.Any:
    if value is None:
        if optional:
            return None
        else:
            raise ValueError(
                f"{name!r} must not be None"
            )

    if not sizes:  # scalar
        return cast_scalar_value(
            name=name,
            value=value,
            class_=class_,
            class_restrictions=class_restrictions,
        )
    else:  # array
        return cast_array_value(
            name=name,
            value=value,
            class_=class_,
            class_restrictions=class_restrictions,
            sizes=sizes,
        )
