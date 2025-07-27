import os
from typing import Optional

ENV_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')


def load_env(path: Optional[str] = None) -> None:
    """Load simple KEY=VALUE lines from a .env file into os.environ.

    Existing environment variables are not overwritten.
    Lines starting with # are ignored.
    """
    env_file = path or ENV_PATH
    if not os.path.exists(env_file):
        return
    with open(env_file) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#') or '=' not in line:
                continue
            key, value = line.split('=', 1)
            os.environ.setdefault(key, value)
