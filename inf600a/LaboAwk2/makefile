###################################
# Fichier makefile pour exercices sur awk.
###################################

# CHANGER LA VALEUR QUI SUIT SELON L'EXERCICE QUE VOUS TRAVAILLEZ!
default: perms

###################################
# Pour aussurer que les permissions soient correctes.
###################################
perms:
	chmod +x *.sh


###################################
# Anonymisation du journal oto.
###################################
anonymes:
	@echo "Test pour anonymes.sh"
	@./anonymes.sh Fichiers/journal-operations.txt > res
	@cat res
	@if diff res Attendus/anonymes.txt; then echo "++ ok ++"; else echo "-- Pas ok --"; fi

###################################
# Version awk de uniq
###################################
uniq:
	@echo "Test pour uniq.sh"
	@./uniq.sh < Fichiers/uniq.txt > res
	@cat res
	@if diff res Attendus/uniq.txt; then echo "++ ok ++"; else echo "-- Pas ok --"; fi

###################################
# Version awk de wc simplifie
###################################
wc:
	@echo "Test pour wc.sh"
	@./wc.sh < Fichiers/avec-blancs.txt > res
	@cat res
	@if diff -w res Attendus/wc.txt; then echo "++ ok ++"; else echo "-- Pas ok --"; fi

###################################
# Nombre d'utilisations d'oto.
###################################
utilisations:
	@echo "Test pour utilisations.sh"
	@./utilisations.sh Fichiers/journal-operations.txt tremblay_gu > res
	@cat res
	@if diff res Attendus/utilisations.txt; then echo "++ ok ++"; else echo "-- Pas ok --"; fi


###################################
# Nettoyage
###################################
clean:
	rm -f res
