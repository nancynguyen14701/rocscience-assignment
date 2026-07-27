import os
import time

from pywinauto import Desktop

POLL_INTERVAL = 0.5


def find_window(title: str, timeout: float = 10.0, exact: bool = False):
    desktop = Desktop(backend="uia")
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        try:
            if exact:
                wins = [w for w in desktop.windows() if w.window_text() == title]
            else:
                wins = [w for w in desktop.windows() if title.lower() in w.window_text().lower()]
            if wins:
                wins[0].wait("ready", timeout=2)
                return wins[0]
        except Exception:
            pass
        time.sleep(POLL_INTERVAL)
    raise TimeoutError(f"Window '{title}' not found within {timeout}s")


def wait_for_file(path: str, timeout: float = 10.0) -> bool:
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        if os.path.isfile(path) and os.path.getsize(path) > 0:
            return True
        time.sleep(POLL_INTERVAL)
    return False


def wait_for_file_content(path: str, expected: str, timeout: float = 10.0) -> bool:
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        try:
            with open(path, "r", encoding="utf-8") as f:
                if expected in f.read():
                    return True
        except (FileNotFoundError, PermissionError):
            pass
        time.sleep(POLL_INTERVAL)
    return False
