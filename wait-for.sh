#!/bin/sh

# wait-for.sh host:port -- command args...

HOST_PORT="$1"
shift

# Skip "--" if present
if [ "$1" = "--" ]; then
  shift
fi

CMD="$@"

# Extract host and port
HOST=$(echo "$HOST_PORT" | cut -d: -f1)
PORT=$(echo "$HOST_PORT" | cut -d: -f2)

until nc -z "$HOST" "$PORT"; do
  echo "Waiting for $HOST:$PORT..."
  sleep 1
done

exec "$@"
