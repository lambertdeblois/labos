###################################
# Fichier makefile pour exercices sur sed, grep, etc.
###################################

# CHANGER LA VALEUR QUI SUIT SELON L'EXERCICE QUE VOUS TRAVAILLEZ!
default: perms


###################################
# Pour aussurer que les permissions soient correctes.
###################################
perms:
	chmod +x *.sh


###################################
# Listage des fichiers qui ont le meme nom et extension.
###################################
lister:
	@./lister-meme-nom-extension.sh Fichiers


###################################
# Suppression de blancs en fin de ligne
###################################
blancs:
	@./supprimer-blancs.sh Fichiers/avec-blancs.txt


###################################
# Recherche d'usagers dans passwd
###################################
usagers:
	@./trouver-usagers.sh


###################################
# Recherche d'enseignants dans log OTO
###################################

enseignants:
	@./trouver-enseignants.sh


###################################
# Recherche d'URLs particuliers
###################################

urls:
	@./trouver-urls.sh


###################################
# Changement de depot git.
#
# 1. make generer
# 2. make remote
# 3. find . -name *.bak
#
# ...
# 0. make reset
# ...
###################################

USAGER=bidon_joe

remote:
	@./changer-remote.sh

generer:
	mkdir Projet1 Projet2 Projet3
	(cd Projet1; git init .; git remote add origin https://malt.labunix.uqam.ca/$(USAGER)/GIT/Projet1)
	(cd Projet2; git init .; git remote add origin https://malt.labunix.uqam.ca/$(USAGER)/GIT/Projet2)
	(cd Projet3; git init .; git remote add origin https://malt.labunix.uqam.ca/$(USAGER)/GIT/Projet3)

reset: clean-all generer

clean-all:
	rm -rf Projet1 Projet2 Projet3
	rm -f Fichiers/*.sans-blanc
	rm -f res-sed res-grep

