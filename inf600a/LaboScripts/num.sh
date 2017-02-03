#!/bin/sh -

###########################################
#
# Script qui affiche le numero de la ligne au debut de chaque ligne
# d'un fichier.
#
# usage:
#   ./num.sh [-k] fichier
#
# L'argument k, optionnel, sert a specifier la largeur du champ a
# utiliser pour les numeros de lignes.
#
# Par exemple, "./num.sh -3 fichier" utilisera trois chiffres pour les
# numeros de ligne.
#
# Evidemment, k doit etre un entier et etre superieur a 0!
#
###########################################


# Fonctions auxiliaires.
function num {
  # Fonction qui recoit un nom de fichier et une largeur positive
  # et qui affiche ensuite le contenu de chacune des lignes avec le
  # numero et l'indentation appropries.
  # A COMPLETER.

  file=$1
  indent=$2
  format="%${indent}d. %s\n"
  awk "{ printf \"$format\", NR, \$0 }" $file
}

function usage {
    echo "usage: "
    echo "  $0 [-k] fichier"
    echo "  Avec k > 0"
    exit 1
}

###################################
# PROGRAMME PRINCIPAL
###################################

[[ $# == 1 || $# == 2 ]] || usage

if [[ $# == 2 ]]
then
  [[ $1 =~ ^-[0-9]+$ ]] || usage
  indent=${1#-}
  [[ $indent != 0 ]] || usage
  shift
fi
file=$1
# On identifie et on valide les arguments.
# A COMPLETER.
#cat -n $1
# Les arguments sont valides, donc:
# - pgm = nom du fichier a traiter
# - largeur = largeur du champ decimal a utiliser pour les numeros de lignes
#             (peut etre vide, auquel cas on utilise la largeur requise par le numero)
# On appelle la fonction auxiliaire qui fait le travail.
num $file $indent
