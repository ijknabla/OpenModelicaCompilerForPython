
import arpeggio  # type: ignore
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import typing
import uuid
import zmq  # type: ignore
from . import parser, visitor, types


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

    def execute(
        self,
        expression: str
    ) -> str:
        self.socket.send_string(expression)
        return self.socket.recv_string()


def parse_omc_value(
    literal: str
):
    return arpeggio.visit_parse_tree(
        parser.omc_value_parser.parse(literal),
        visitor.OMCValueVisitor()
    )


def parse_defaultValueInfoDict(
    interface: str
) -> typing.Dict[types.Identifier, typing.Optional[str]]:
    return dict(
        arpeggio.visit_parse_tree(
            parser.stored_definition_parser.parse(interface),
            visitor.DefaultValueInfoVisitor(),
        )
    )
