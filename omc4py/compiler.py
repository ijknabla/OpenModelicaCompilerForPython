from __future__ import annotations

import logging
import shutil
import tempfile
import uuid
import warnings
from collections.abc import Iterator, Sequence
from contextlib import ExitStack, suppress
from dataclasses import dataclass, field
from os import PathLike
from pathlib import Path
from subprocess import DEVNULL, PIPE, Popen
from typing import TYPE_CHECKING, Any, Optional, Union, overload

import zmq.asyncio

from . import classes, exception, string
from ._util import terminating, unlinking
from .parser import parse_OMCExceptions

logger = logging.getLogger(__name__)

if TYPE_CHECKING:
    Process = Popen[str]
    StrOrPathLike = Union[str, PathLike[str]]


@overload
def _enter_zmq_context(
    context_type: type[zmq.Context],
    omc_command: Optional[StrOrPathLike] = None,
) -> tuple[Process, zmq.Socket, ExitStack]:
    ...


@overload
def _enter_zmq_context(
    context_type: type[zmq.asyncio.Context],
    omc_command: Optional[StrOrPathLike] = None,
) -> tuple[Process, zmq.asyncio.Socket, ExitStack]:
    ...


def _enter_zmq_context(
    context_type: type[zmq.Context | zmq.asyncio.Context],
    omc_command: Optional[StrOrPathLike] = None,
) -> tuple[Process, zmq.Socket | zmq.asyncio.Socket, ExitStack]:
    stack = ExitStack()
    if omc_command is None:
        omc_command = "omc"

    suffix = str(uuid.uuid4())

    command = [
        str(resolve_command(omc_command)),
        "--interactive=zmq",
        "--locale=C",
        f"-z={suffix}",
    ]

    stack.callback(lambda: logger.info(f"(pid={process.pid}) Stop omc"))
    process = stack.enter_context(
        terminating(
            Popen(
                command,
                stdout=PIPE,
                stderr=DEVNULL,
                encoding="utf-8",
            )
        )
    )
    assert process.stdout is not None

    logger.info(f"(pid={process.pid}) Start omc :: {' '.join(command)}")

    first_line = process.stdout.readline()
    logger.debug(f"(pid={process.pid}) >>> {first_line}")

    with unlinking(
        find_openmodelica_zmq_port_filepath(suffix)
    ) as port_filepath:
        logger.info(
            f"(pid={process.pid}) Find zmq port file at {port_filepath}"
        )
        port = port_filepath.read_text()
    logger.info(f"(pid={process.pid}) Remove zmq port file at {port_filepath}")

    stack.callback(
        lambda: logger.info(f"(pid={process.pid}) Close zmq sokcet")
    )
    socket: zmq.Socket | zmq.asyncio.Socket
    socket = context_type().socket(zmq.REQ)
    stack.enter_context(socket)
    socket.connect(port)
    logger.info(f"(pid={process.pid}) Connect zmq sokcet via {port}")

    return process, socket, stack


def resolve_command(
    command: StrOrPathLike,
) -> Path:
    executable = shutil.which(command)
    if executable is None:
        raise FileNotFoundError(f"Can't find executable of {command}")

    return Path(executable).resolve()


def find_openmodelica_zmq_port_filepath(suffix: Optional[str]) -> Path:
    temp_dir = Path(tempfile.gettempdir())

    pattern_of_name = "openmodelica*.port"
    if suffix is not None:
        pattern_of_name += f".{suffix}"

    candidates = tuple(temp_dir.glob(pattern_of_name))

    if not candidates:
        raise ValueError(
            f"Can't find openmodelica port file " f"at {temp_dir}"
        )
    elif len(candidates) >= 2:
        raise ValueError(
            f"Ambiguous openmodelica port file {candidates}" f"at {temp_dir}"
        )

    return candidates[0]


@dataclass(frozen=True)
class OMCInteractive(
    classes.AbstractOMCInteractive,
):
    process: Process
    socket: zmq.Socket
    stack: ExitStack = field(repr=False)

    @classmethod
    def open(
        cls,
        omc_command: Optional[StrOrPathLike] = None,
    ) -> "OMCInteractive":
        process, socket, stack = _enter_zmq_context(zmq.Context, omc_command)
        return cls(process=process, socket=socket, stack=stack)

    def close(
        self,
    ) -> None:
        with suppress(Exception):
            self.stack.close()

    def evaluate(self, expression: str) -> str:
        logger.debug(f"(pid={self.process.pid}) >>> {expression}")
        self.socket.send_string(expression)
        result = self.socket.recv_string()
        logger.debug(f"(pid={self.process.pid}) {result}")
        return result

    def call_function(
        self,
        funcName: str,
        inputArguments: Sequence[classes.InputArgument],
        outputArguments: Sequence[classes.OutputArgument],
        parser: classes.Parser,
    ) -> Any:
        def arguments() -> Iterator[str]:
            to_keyword_argument = False
            for component, name, value, required in inputArguments:
                to_keyword_argument |= required == "optional"

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
                funcName=funcName, argument_list=", ".join(arguments())
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
                raise exception.OMCRuntimeError(result_literal) from None
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
            (
                (
                    component,
                    name,
                ),
            ) = outputArguments
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
