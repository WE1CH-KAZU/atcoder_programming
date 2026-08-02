#!/bin/sh
SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)
exec uv run python "$SCRIPT_DIR/tools/create_new_contest.py" "$@"
