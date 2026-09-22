import os
import shutil
import signal
import subprocess
import time

from fasthtml.common import Style, serve

from app.core.database import app
from app import routes as _routes
DEFAULT_PORT = int(os.environ.get("PORT", 5001))


def _terminate_pid(pid: str) -> None:
    try:
        os.kill(int(pid), signal.SIGTERM)
    except (ProcessLookupError, PermissionError):
        return

    deadline = time.monotonic() + 2
    while time.monotonic() < deadline:
        try:
            os.kill(int(pid), 0)
        except ProcessLookupError:
            return
        time.sleep(0.1)

    try:
        os.kill(int(pid), signal.SIGKILL)
    except (ProcessLookupError, PermissionError):
        return


def kill_processes_on_port(port: int) -> None:
    if port is None:
        return

    lsof_path = shutil.which("lsof")
    if lsof_path:
        result = subprocess.run(
            [lsof_path, "-ti", f"tcp:{port}"],
            capture_output=True,
            text=True,
            check=False,
        )
        pids = [pid for pid in result.stdout.split() if pid.strip().isdigit()]
        if pids:
            for pid in pids:
                _terminate_pid(pid)
            return

    fuser_path = shutil.which("fuser")
    if fuser_path:
        subprocess.run(
            [fuser_path, "-k", f"{port}/tcp"],
            capture_output=True,
            text=True,
            check=False,
        )





if __name__ == "__main__":
    kill_processes_on_port(DEFAULT_PORT)
    serve(appname="main", app="app", port=DEFAULT_PORT)
