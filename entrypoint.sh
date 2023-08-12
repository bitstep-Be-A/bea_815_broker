#!/bin/bash
set -e

echo "setting environment..."
if [[ -f .env ]]; then
  export $(cat .env | grep -v '^#' | xargs)
fi

echo "server start"

uvicorn main:app --host 0.0.0.0 --port 7860
