
import atexit
import logging
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import typing
import typing_extensions
import uuid
import warnings
import zmq  # type: ignore

from . import (
    classes,
    exception,
    string,
)

from .parser import parse_OMCExceptions


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

                value = component.cast(name, value, required)
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

        # return None if result_literal == "\n"
        if not result_literal or result_literal.isspace():
            return None

        try:
            result_value = parser(result_literal)
        except Exception:
            excs = list(parse_OMCExceptions(result_literal))
            if not excs:
                raise exception.OMCRuntimeError(
                    result_literal
                ) from None
            else:
                for exc in excs:
                    if isinstance(exc, Warning):
                        warnings.warn(exc)
                    else:
                        raise exc from None
                else:
                    return

        if len(outputArguments) == 0:
            raise ValueError(
                "There is no output variable in the function, "
                f"but omc returns {result_value!r}"
            )
        elif len(outputArguments) == 1:
            (component, name,), = outputArguments
            return component.cast(name, result_value)
        else:
            if len(result_value) != len(outputArguments):
                raise ValueError(
                    f"Size of result must be [{len(outputArguments)}], "
                    f"got {result_value!r} size is [{len(result_value)}]"
                )
            return tuple(
                component.cast(name, value)
                for (component, name), value in zip(
                    outputArguments, result_value
                )
            )


atexit.register(OMCInteractive.close_all)
