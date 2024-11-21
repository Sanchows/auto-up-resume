#!/bin/sh

# cron has its own virtual environment and hasn't access to global environment.
# Then we are setting up env variables to script directly

set -a
. /app/.env
set +a
PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 /usr/local/bin/python /app