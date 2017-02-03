#!/bin/sh -

###################################################################
# Script qui affiche la definition d'une function.
#
# usage:
#   $0 nomDeFonction [fichier]
#
# Si aucun fichier n'est specifie, alors le script fouille dans tous
# les fichiers *.sh accessibles a partir du repertoire courant (donc
# fouille aussi dans les sous-repertoires). Dans ce cas, le nom du
# fichier est affiche avant que la definition de la fonction ne soit
# affichee.
#
# Si un fichier est explicitement specifie, alors seul ce fichier est
# fouille pour trouver la definition et le nom de fichier n'est pas
# affiche.
#
# *Hypotheses*:
#  - Les fonctions sont toujours definies avec le mot-cle "function";
#  - Le nom de la fonction est toujours sur la meme ligne que "function";
#  - La fin de la fonction est indiquee par un "}" final
#    qui apparait toujours en tout debut de ligne.
#
# Remarque: Pour matcher le nom complet de la fonction, et rien d'autre:
#  - Linux: Utilise \b
#  - Mac OS: Solution sans \b car n'est pas disponible
#
###################################################################

function usage {
    echo "usage:"
    echo "$0 nomDeFonction [fichier]"
    exit 1
}

[[ $# == 1 || $# == 2 ]] || usage

delim_debut="^[ ]*function[ ][ ]*$1[ ]"
delim_fin="^}"

if [[ $# == 1 ]]; then
  liste_fichs=$( find . -name '*.sh')
elif [[ $# == 2 ]]; then
  liste_fichs=$2
fi

for fich in $liste_fichs
do
  sed -n "/$delim_debut/,/$delim_fin/p" $fich
done


#if [[ $# == 2 && $( cat $2 | grep "function $1 ") ]]
#then
#  debut_fonction="^[ ]*function[ ][ ]*$1[ ]"
#  fin_function="^}"
#  echo $2 | sed -n "/$debut_fonction/,/$fin_function/"
#fi
