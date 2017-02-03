#coding utf8
#labo2

import sqlite3

connection = sqlite3.connect('musique.db')
cursor = connection.cursor()
fichier = open("ajouter.txt", 'r')
for each in fichier:
    artiste, album, annee = each.strip().split('|')
    cursor.execute("select id from artiste where nom = ?", (artiste,))
    data = cursor.fetchone()
    if data is None:
        cursor.execute("insert into artiste(nom, est_solo, nombre_individus) values (?, ?, ?)", (artiste, True, 1))
        cursor.execute("select * from artiste")
        nb = cursor.fetchall()
        print len(nb)
        cursor.execute("insert into album(titre, annee, artiste_id, maison_disque_id) values (?, ?, ?, ?)", (album, annee, len(nb), 1))
    else:
        cursor.execute("insert into album(titre, annee, artiste_id, maison_disque_id) values (?, ?, ?, ?)", (album, annee, data[0], 1))
    connection.commit()

    print "%s, %s, %d" % (artiste, album, int(annee))



connection.close()
