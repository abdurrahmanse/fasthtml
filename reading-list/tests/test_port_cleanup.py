import socket
import subprocess
import time

from app import config
from main import kill_processes_on_port


def _find_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def test_kill_processes_on_port():
    port = _find_free_port()
    proc = subprocess.Popen(
        [
            "python",
            "-c",
            "import socket, time; s = socket.socket(); s.bind(('127.0.0.1', " + str(port) + ")); s.listen(); time.sleep(30)",
        ]
    )

    time.sleep(0.5)
    kill_processes_on_port(port)
    time.sleep(0.5)

    assert proc.poll() is not None
