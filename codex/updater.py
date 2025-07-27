#!/usr/bin/env python3
"""Update README and history log with new philosophical thoughts."""

import os
import sys

from utils import load_env

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
README_PATH = os.path.join(BASE_DIR, "README.md")
load_env()

LOG_FILE = os.getenv("LOG_FILE", os.path.join(BASE_DIR, "logs", "history.log"))
UPDATE_README = os.getenv("UPDATE_README", "1")


def append_content(content: str) -> None:
    """Append content to README and log file if configured."""
    if not content:
        return
    if UPDATE_README == "1":
        with open(README_PATH, "a") as readme:
            readme.write("\n" + content.strip() + "\n")
    if LOG_FILE:
        os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
        with open(LOG_FILE, "a") as log:
            log.write(content.strip() + "\n")


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            content = f.read()
    else:
        content = sys.stdin.read()
    append_content(content)


if __name__ == '__main__':
    main()
