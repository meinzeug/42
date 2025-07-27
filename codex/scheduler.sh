#!/usr/bin/env bash
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Load environment variables if a .env file exists
ENV_FILE="${DIR}/../.env"
if [[ -f "$ENV_FILE" ]]; then
    set -o allexport
    source "$ENV_FILE"
    set +o allexport
fi

THOUGHT="$(${DIR}/thinker.py)"

echo "$THOUGHT" | ${DIR}/updater.py
