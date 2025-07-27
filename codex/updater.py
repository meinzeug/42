#!/usr/bin/env python3
import os
import sys

README_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'README.md')
LOG_FILE = os.getenv('LOG_FILE', 'logs/history.log')


def append_content(content: str):
    if not content:
        return
    with open(README_PATH, 'a') as readme:
        readme.write('\n' + content.strip() + '\n')
    if LOG_FILE:
        os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
        with open(LOG_FILE, 'a') as log:
            log.write(content.strip() + '\n')


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as f:
            content = f.read()
    else:
        content = sys.stdin.read()
    append_content(content)


if __name__ == '__main__':
    main()
