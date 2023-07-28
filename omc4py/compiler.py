from __future__ import annotations

import logging
import shutil
import tempfile
import uuid
from collections.abc import Generator
from contextlib import ExitStack, contextmanager
from os import PathLike
from pathlib import Path
from subprocess import DEVNULL, PIPE, Popen
from typing import TYPE_CHECKING, Optional, Union

from ._util import terminating, unlinking

logger = logging.getLogger(__name__)

if TYPE_CHECKING:
    Process = Popen[str]
    StrOrPathLike = Union[str, PathLike[str]]


@contextmanager
def _create_omc_interactive(
    omc_command: StrOrPathLike,
) -> Generator[tuple[Process, str], None, None]:
    with ExitStack() as stack:
        suffix = str(uuid.uuid4())

        command = [
            f"{_resolve_command(omc_command)}",
            "--interactive=zmq",
            "--locale=C",
            f"-z={suffix}",
        ]

        stack.callback(lambda: logger.info(f"(pid={process.pid}) Stop omc"))
        process = stack.enter_context(
            terminating(
                Popen(command, stdout=PIPE, stderr=DEVNULL, encoding="utf-8")
            )
        )
        assert process.stdout is not None
        logger.info(f"(pid={process.pid}) Start omc :: {' '.join(command)}")

        first_line = process.stdout.readline()
        logger.debug(f"(pid={process.pid}) >>> {first_line}")

        with unlinking(
            _find_openmodelica_zmq_port_filepath(suffix)
        ) as port_filepath:
            logger.info(
                f"(pid={process.pid}) Find zmq port file at {port_filepath}"
            )
            port = port_filepath.read_text()
        logger.info(
            f"(pid={process.pid}) Remove zmq port file at {port_filepath}"
        )

        yield process, port


def _resolve_command(
    command: StrOrPathLike,
) -> Path:
    executable = shutil.which(command)
    if executable is None:
        raise FileNotFoundError(f"Can't find executable of {command}")

    return Path(executable).resolve()


def _find_openmodelica_zmq_port_filepath(suffix: Optional[str]) -> Path:
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
