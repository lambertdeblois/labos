#!/bin/sh -

# Script qui emule uniq, mais mis en oeuvre en utilisant awk.
#
# Fonctionne uniquement pour stdin.

#cat $1 | awk '!seen[$0]++'

cat $1 | awk ' $0!=derniere_ligne { print }
                          { derniere_ligne = $0 }'
