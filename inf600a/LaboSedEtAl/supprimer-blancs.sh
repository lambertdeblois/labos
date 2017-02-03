#! /bin/sh -

##################################################################
# Supprimer les blancs en fin de ligne dans un fichier
##################################################################

if [[ $# == 0 ]]; then
    echo "usage:"
    echo "$0 nomDeFichier"
    exit -1
fi

FICHIER=$1

# A COMPLETER!
cp $FICHIER $FICHIER.sans-blanc
sed -i 's/[[:blank:]]*$//' $FICHIER.sans-blanc

echo ""
echo "** Appel a diff ordinaire: on devrait voir des differences"
diff $FICHIER $FICHIER.sans-blanc
echo ""
echo "** Appel a diff en ignorant les blancs: on ne devrait pas voir de differences"
diff -b $FICHIER $FICHIER.sans-blanc
