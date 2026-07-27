from pathlib import Path


def file_exists(path):
    return Path(path).exists()


def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()