
from pathlib import Path
import os
import subprocess
import tempfile
import typing
import uuid
import zmq


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
        omc_executable: typing.Optional[os.PathLike] = None,
    ) -> "InteractiveOMC":
        executable: str
        if omc_executable is None:
            executable = "omc"
        else:
            executable = os.fspath(omc_executable)

        suffix = str(uuid.uuid4())

        socket = zmq.Context().socket(
            # pylint: disable=no-member
            zmq.REQ
        )

        process = subprocess.Popen(
            [executable, "--interactive=zmq", f"-z={suffix}"],
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
        port = find_openmodelica_zmq_port_filepath(suffix).read_text()

        self.socket.connect(port)

    def close(
        self
    ) -> None:
        self.socket.close()
        self.process.terminate()

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
