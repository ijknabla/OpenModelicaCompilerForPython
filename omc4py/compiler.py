
import atexit
import logging
import numpy  # type: ignore
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import typing
import typing_extensions
import uuid
import zmq  # type: ignore

from . import (
    classes,
    string,
)


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


def cast_value(
    component: classes.Component,
    name: str,
    value: typing.Any,
    required: classes.REQUIRED_or_OPTIONAL = "required",
) -> typing.Any:
    if value is None:
        if required == "required":
            raise ValueError(
                f"{name!r} must not be None"
            )
        if required == "optional":
            return None
        else:
            raise ValueError(
                f"required must be (required|optional) got {required!r}"
            )

    if not component.dimensions:  # scalar
        class_restrictions = get_class_restrictions(component)
        if class_restrictions:
            if not isinstance(value, class_restrictions):
                raise TypeError(
                    f"{name!r} must be an instance of {class_restrictions}"
                    f", got {value!r}: {type(value)!r}"
                )
        return component.class_(value)

    else:  # array
        return cast_array_value(
            component,
            name,
            value,
        )


def cast_array_value(
    component: classes.Component,
    name: str,
    value: typing.Any,
) -> numpy.ndarray:
    object_array = numpy.array(value, dtype=object)

    same_n_dimensions = (len(component.dimensions) == object_array.ndim)
    dimensions_are_correct = [
        True if expected is None else expected == actual
        for expected, actual in zip(component.dimensions, object_array.shape)
    ]

    if not(same_n_dimensions and all(dimensions_are_correct)):
        raise ValueError(
            "Shape of the array "
            f"must be {dimensions_to_str(component.dimensions)}, "
            f"got {dimensions_to_str(object_array.shape)}"
        )

    class_restrictions = get_class_restrictions(component)
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
        component.class_,
        otypes=[numpy.dtype(component.class_)]
    )
    return class_vectorized(object_array)


def dimensions_to_str(
    sizes: classes.Dimensions,
) -> str:
    return (
        "{"
        + ", ".join(
            str(size) if size is not None else ":"
            for size in sizes
        )
        + "}"
    )


def get_class_restrictions(
    component: classes.Component,
) -> typing.Tuple[typing.Type, ...]:
    if component.class_ is classes.Real:
        return (classes.Real, float)
    elif component.class_ is classes.Integer:
        return (classes.Integer, int)
    elif component.class_ is classes.Boolean:
        return (classes.Boolean, bool)
    elif component.class_ is classes.String:
        return (classes.String, str)
    elif component.class_ is classes.TypeName:
        return (classes.TypeName, str)
    elif component.class_ is classes.VariableName:
        return (classes.VariableName, str)
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
        parser: classes.Parser,
    ) -> typing.Any:
        def arguments() -> typing.Iterator[str]:
            to_keyword_argument = False
            for component, name, value, required in inputArguments:
                to_keyword_argument |= (required == "optional")

                value = cast_value(component, name, value, required)
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
            if result_literal and not result_literal.isspace():
                raise ValueError(
                    f"Unexpected result, got {result_literal!r}"
                )
            return

        result_value = parser(result_literal)

        if len(outputArguments) == 1:
            (component, name,), = outputArguments
            return cast_value(component, name, result_value)
        else:
            return tuple(
                cast_value(component, name, value)
                for (component, name), value in zip(
                    outputArguments, result_value
                )
            )


atexit.register(OMCInteractive.close_all)
