#!/bin/sh -

# Script qui emule wc, mais mis en oeuvre en utilisant awk.
# Fonctionne uniquement pour stdin.


echo 0 0 0  # A COMPLETER

cat $1 | awk ' {mots += NF; c +=length($0)+1}
              END { print "Lignes =", NR, "Mots =", mots, "Lenght =", c }'
