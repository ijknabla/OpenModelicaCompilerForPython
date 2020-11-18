
import atexit
import logging
import numpy  # type: ignore
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import typing
import typing_extensions
import uuid
import zmq  # type: ignore

from . import (
    classes,
    exception,
    parser,
    string,
    types,
)


logger = logging.getLogger(__name__)


omc_error_pattern = re.compile(
    r"(\[(?P<info>[^]]*)\]\s+)?(?P<kind>\w+):\s+(?P<message>.*)"
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


def get_class_restrictions(
    component: classes.Component,
) -> typing.Tuple[typing.Type, ...]:
    if component.class_ is types.Real:
        return (types.Real, float)
    elif component.class_ is types.Integer:
        return (types.Integer, int)
    elif component.class_ is types.Boolean:
        return (types.Boolean, bool)
    elif component.class_ is types.String:
        return (types.String, str)
    elif component.class_ is types.TypeName:
        return (types.TypeName, str)
    elif component.class_ is types.VariableName:
        return (types.VariableName, str)
    else:
        return ()


class OMCInteractive(
    classes.AbstractOMCInteractive,
):
    __slots__ = (
        "__socket",
        "__process",
    )

    __instances: typing_extensions.Final[typing.Set["OMCInteractive"]] \
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
    ) -> "OMCInteractive":
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
            f"(pid={self.process.pid}) "
            f"Find zmq port file at {port_filepath}"
        )

        try:
            port = port_filepath.read_text()
            self.socket.connect(port)
            logger.info(
                f"(pid={self.process.pid}) "
                f"Connect zmq sokcet via {port}"
            )
        finally:
            try:
                port_filepath.unlink()
                logger.info(
                    f"(pid={self.process.pid}) "
                    f"Remove zmq port file at {port_filepath}"
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

    def call_function(
        self,
        funcName: str,
        inputArguments: typing.Sequence[classes.InputArgument],
        outputArguments: typing.Sequence[classes.OutputArgument],
    ) -> typing.Any:
        def arguments() -> typing.Iterator[str]:
            to_keyword_argument = False
            for component, name, value, required in inputArguments:
                is_optional = (required == "optional")
                to_keyword_argument |= is_optional
                value = cast_value(
                    name,
                    value,
                    is_optional,
                    component.class_,
                    get_class_restrictions(component),
                    component.dimensions,
                )
                if value is None:
                    continue

                literal = string.to_omc_literal(value)

                if to_keyword_argument:
                    yield f"{name!s} = {literal!s}"
                else:
                    yield f"{literal!s}"

        result_literal = self.evaluate(
            "{funcName}({argument_list})".format(
                funcName=funcName,
                argument_list=", ".join(arguments())
            )
        )

        if not outputArguments:
            if not (not result_literal or result_literal.isspace()):
                raise ValueError(
                    "Unexpected result, got {result_literal!r}"
                )
            return

        result_value = parser.parse_OMCValue(result_literal)
        if len(outputArguments) == 1:
            (component, name,), = outputArguments
            return cast_value(
                name,
                result_value,
                False,
                component.class_,
                (),
                component.dimensions,
            )
        else:
            return tuple(
                cast_value(
                    name,
                    value,
                    False,
                    component.class_,
                    (),
                    component.dimensions,
                )
                for (component, name), value in zip(
                    outputArguments, result_value
                )
            )

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


atexit.register(OMCInteractive.close_all)
