import sqlite3
import datetime

def build_user_dictionnary(row):
    return {"nom": row[0], "prenom": row[1], "courriel": row[2],
            "date_inscription": row[3], "salt": row[4], "hash": row[5]}




class Database:
    def __init__(self):
        self.connection = None

    def get_connection(self):
        if self.connection is None:
            self.connection = sqlite3.connect('db/utilisateur.bd')
        return self.connection

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()

    def get_users(self):
        cursor = self.get_connection().cursor()
        cursor.execute("select * from utilisateur")
        users = cursor.fetchall()
        return [build_user_dictionnary(each) for each in users]

    def insert_user(self, user):
        connection = self.get_connection()
        cursor = connection.cursor()
        cursor.execute(("insert into utilisateur (nom, prenom, courriel,\
         date_inscription, salt, hash) values (?, ?, ?, ?, ?, ?)\
         "), (user[0], user[1], user[2], datetime.date.today(), user[3], user[4]))
        connection.commit()
