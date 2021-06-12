#!/bin/sh
echo $0 $1

if [ -z "$1" ]; then
	echo "Missing argument; executing source!"
	. ./env_vars.sh
	exec "$@"
fi
if echo "$1" | egrep -q ^"prod*"; then
	echo "move .env.prod to .env"
	mv .env.prod .env
fi
if echo "$1" | egrep -q ^"dev*"; then
	echo "move .env.dev to .env"
	mv .env.dev .env
fi
if echo "$1" | egrep -q ^"test*"; then
	echo "move .env.test to .env"
	mv .env.test .env
fi
echo "Executed entry-point with $1 build-arg"
