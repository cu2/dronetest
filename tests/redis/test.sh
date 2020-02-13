#!/usr/bin/env bash
set -euo pipefail

HOST=$1


PONG=`redis-cli -h $HOST ping | grep PONG`
while [ -z "$PONG" ]; do
  sleep 1
  echo "Retry Redis ping... "
  PONG=`redis-cli -h $HOST ping | grep PONG`
done
