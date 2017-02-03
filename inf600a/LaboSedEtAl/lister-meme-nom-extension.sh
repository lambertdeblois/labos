#! /bin/sh -

##################################################################
# Lister les fichiers du repertoire dont le nom et l'extension sont identiques.
# Cherche dans le repertoire courant si aucun repertoire n'est specifie.
##################################################################

if [[ $# == 0 ]]; then
    REPERTOIRE='.'
else
    REPERTOIRE=$1
fi

for ENTRY in $REPERTOIRE/*

do
filename=$(basename $ENTRY)
  #printf ${filename%.*}
  #printf ${ENTRY#*.}
  if [[ ${filename%.*} == ${ENTRY#*.} ]]; then
    echo $filename
  fi
done
