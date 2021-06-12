#!/bin/sh
echo $0 $1

if [ -z "$1" ] ; then
	echo "Missing argument; executing source!"
	. ./env_vars.sh
	exec "$@"
fi
if echo "$1" | egrep -q ^"prod*" ; then
	echo "move .env.prod to .env"
	mv .env.prod .env
elif echo "$1" | egrep -q ^"dev*" ; then
	echo "move .env.local to .env"
	mv .env.local .env
elif echo "$1" | egrep -q ^"stag*" ; then
	echo "move .env.stagging to .env"
	mv .env.stagging .env
elif echo "$1" | egrep -q ^"ind*" ; then
	echo "move .env.india to .env"
	mv .env.india .env
else
	echo "No environment matched with $1, executing source!"
	. ./env_vars.sh
	exec "$@"
fi
echo "Executed entry-point with $1 build-arg"
