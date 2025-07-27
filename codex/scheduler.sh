#!/usr/bin/env bash
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

THOUGHT="$(${DIR}/thinker.py)"

echo "$THOUGHT" | ${DIR}/updater.py
