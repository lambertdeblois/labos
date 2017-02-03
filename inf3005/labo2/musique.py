#coding utf8
#labo2

import sqlite3

connection = sqlite3.connect('musique.db')
cursor = connection.cursor()
cursor.execute("select * from artiste")
for row in cursor:
    identifier, nom, boolean, nb_individus = row
    print "%d, %s, %d, %d" % (identifier, nom, boolean, nb_individus)


print ""
cursor.execute("select * from album")
for row in cursor:
    identifier, titre, annee, artiste_id, maison_disque_id = row
    print "%d, %s, %d, %d, %d" % (identifier, titre, annee, artiste_id, maison_disque_id)


numero = raw_input("\nQuel artiste voulez-vous voir?")
int(numero)

cursor.execute("select * from album where artiste_id = ?", numero)

for row in cursor:
    identifier, titre, annee, artiste_id, maison_disque_id = row
    print "%s, %d" %(titre, annee)


connection.close()
