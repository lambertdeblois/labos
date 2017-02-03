###################################
# Fichier makefile pour labo sur les scripts.
###################################

.IGNORE:

#################################################
# A modifier, selon exercice + exemple ou tests.

# Exercice 1.
WIP=tf

# Exercice 2.
#WIP=num

# Pour executer l'exemple.
wip: wip_ex

# Pour executer les "vrais" tests.
#wip: wip_test

#################################################

wip_ex: exemple_$(WIP)

wip_test: tests_$(WIP)

exemples: exemple_num exemple_tf

tests: tests_num tests_tf

###################################
# Ajout de numeros de ligne.
###################################
exemple_num:
	# Devrait emettre ce qui suit:
	# 1. #!
	# 2. function usage {
	# 3.     echo "usage"
	# 4. }
	# 5. 
	# . function usager {
	# 7.     echo "usager"
	# 8. }
	@./num.sh -2 Fichiers/n1.sh

tests_num: tests_num_ok tests_num_erreurs
	@echo "*** Fin tests_num: OK ***"

tests_num_ok:
	@./num.sh Fichiers/n1.sh > obtenu.txt
	@diff Attendus/test1.txt obtenu.txt
	@./num.sh -5 Fichiers/n1.sh > obtenu.txt
	@diff Attendus/test2.txt obtenu.txt

tests_num_erreurs:
	# "Test avec -x (k non numerique)"
	@if ./num.sh -x Fichiers/n1.sh &> obtenu.txt; then echo "*** Valeur exit incorrecte"; else true; fi
	@diff Attendus/usage-num.txt obtenu.txt

	# "Test avec -0 (k = 0)"
	@if ./num.sh -0 Fichiers/n1.sh &> obtenu.txt; then echo "*** Valeur exit incorrecte"; else true; fi
	@diff Attendus/usage-num.txt obtenu.txt

	# "Test avec 2 (pas de '-')"
	@if ./num.sh 2 Fichiers/n1.sh &> obtenu.txt; then echo "*** Valeur exit incorrecte"; else true; fi
	@diff Attendus/usage-num.txt obtenu.txt

###################################
# Recherche de functions
###################################

exemple_tf:
	# Devrait emettre ce qui suit:
	# function usager {
	#    echo "usager"
	# }
	@./tf.sh usager Fichiers/n1.sh

tests_tf:
	@./tf.sh usage Fichiers/n1.sh > obtenu.txt
	@diff Attendus/tf1.txt obtenu.txt

	@./tf.sh usage > obtenu.txt > obtenu.txt
	@diff Attendus/tf2.txt obtenu.txt

	@./tf.sh foo > obtenu.txt
	@diff Attendus/tf3.txt obtenu.txt
	@echo "*** Fin tests_tf: OK ***"

clean:
	rm -f *~
	rm -f obtenu.txt

