#!/bin/sh -

# Script utilisant awk pour creer une version du journal Oto anonyme,
# i.e., sans les noms d'utilisateurs.

if [[ -z $1 ]]; then
    echo "*** Il faut specifier un fichier en argument" >&2
    exit -1
fi
fich="$1"

cat $fich | awk -F '|' '{ print $1, "|", $2 "|", $4 }'
