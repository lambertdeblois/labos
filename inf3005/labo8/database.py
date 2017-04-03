import sqlite3


class Database:
    def __init__(self):
        self.connection = None

    def get_connection(self):
        if self.connection is None:
            self.connection = sqlite3.connect('db/livres.db')
        return self.connection

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()

    def get_livres(self):
        cursor = self.get_connection().cursor()
        cursor.execute("select * from livres")
        livres = cursor.fetchall()
        return [(un_livre[0], un_livre[1], un_livre[2], un_livre[3], un_livre[4], un_livre[5]) for un_livre in livres]

    def get_livre(self, identifiant):
        cursor = self.get_connection().cursor()
        cursor.execute("select * from livres where id_livre = ?", identifiant)
        livre = cursor.fetchone()
        return livre[0], livre[1], livre[2], livre[3], livre[4], livre[5]

    def creer_livre(self, data):
        connexion = self.get_connection()
        cursor = connexion.cursor()
        cursor.execute("insert into livres (auteur, titre, annee_pub, nb_pages, nb_chapitres) values (?, ?, ?, ?, ?)", (data["auteur"], data["titre"], data["annee_pub"], data["nb_pages"], data["nb_chapitres"]))
        connexion.commit()

    def delete_livre(self, identifiant):
        connexion = self.get_connection()
        cursor = connexion.cursor()
        cursor.execute("delete from livres where id_livre = ?", identifiant)
        connexion.commit()
