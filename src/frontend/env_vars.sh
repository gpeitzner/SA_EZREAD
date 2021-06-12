#!/bin/sh
#
#
#	Export .env vars to local env
#
while read -r line || [ -n "$line" ]; do
	if $(printf '%s\n' "$line" | grep -q -e '='); then
		varname=$(printf '%s\n' "$line" | sed -e 's/=.*//')
		varvalue=$(printf '%s\n' "$line" | sed -e 's/^[^=]*=//')
	fi
	eval vvarname="\$$varname"
	value=$(printf '%s\n' "${vvarname}")
	[ -z $value ] && value=${varvalue}
	export ${varname}=${value}
	echo ${varname}=${value}
done <.env
echo "env_vars loaded"
