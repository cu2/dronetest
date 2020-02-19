#!/usr/bin/env bash

HOST=$1


CNT=0
PONG=`redis-cli -h $HOST ping | grep PONG`
while [[ -z "$PONG" && "$CNT" -lt 10 ]]; do
  sleep 1
  echo "Retry Redis ping... "
  PONG=`redis-cli -h $HOST ping | grep PONG`
  CNT=$((CNT+1))
done
