#!/bin/sh -

# Script utilisant awk pour determiner le nombre de fois ou un
# utilisateur donne a utiliser Oto, tel qu'indique dans le journal des operations.

if [[ -z $1 ]] || [[ -z $2 ]]; then
    echo "*** Il faut specifier le journal et un nom d'usager" >&2
    exit -1
fi

journal="$1"
usager="$2"

echo "$usager: 0"   # A COMPLETER

cat $1 | awk "/$usager/ { count += 1 }
                    END { print count}"
