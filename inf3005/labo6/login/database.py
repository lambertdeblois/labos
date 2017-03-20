# coding: utf8

# Copyright 2017 Jacques Berger
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import sqlite3


class Database:
    def __init__(self):
        self.connection = None

    def get_connection(self):
        if self.connection is None:
            self.connection = sqlite3.connect('db/users.db')
        return self.connection

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()

    def create_user(self, username, prenom, nom, email, salt, hashed_password):
        connection = self.get_connection()
        connection.execute(("insert into users(utilisateur, prenom, nom, email, salt, hash)"
                            " values(?, ?, ?, ?, ?, ?)"), (username, prenom, nom, email, salt,
                                                     hashed_password))
        connection.commit()

    def get_user_login_info(self, username):
        cursor = self.get_connection().cursor()
        cursor.execute(("select salt, hash from users where utilisateur=?"),
                       (username,))
        user = cursor.fetchone()
        if user is None:
            return None
        else:
            return user[0], user[1]

    def save_session(self, id_session, username):
        connection = self.get_connection()
        connection.execute(("insert into sessions(id_session, utilisateur) "
                            "values(?, ?)"), (id_session, username))
        connection.commit()

    def delete_session(self, id_session):
        connection = self.get_connection()
        connection.execute(("delete from sessions where id_session=?"),
                           (id_session,))
        connection.commit()

    def get_session(self, id_session):
        cursor = self.get_connection().cursor()
        cursor.execute(("select utilisateur from sessions where id_session=?"),
                       (id_session,))
        data = cursor.fetchone()
        if data is None:
            return None
        else:
            return data[0]


    def get_name_fname_confirmed(self, username):
        cursor = self.get_connection().cursor()
        cursor.execute(("select prenom, nom, confirmed from users where utilisateur=?"),
                        (username,))
        data = cursor.fetchone()
        if data is None:
            return None
        else:
            return data[0], data[1], data[2]

    def get_token(self, token):
        cursor = self.get_connection().cursor()
        cursor.execute("select token from users where token=?", (token,))
        token = cursor.fetchone()
        if token is None:
            return None
        else:
            return token[0]

    def set_token(self, token, username):
        connection = self.get_connection()
        connection.execute(("update users set token=? where utilisateur=?"), ( token, username))
        connection.commit()


    def set_confirmation_email(self, token):
        connection = self.get_connection()
        connection.execute(("update users set confirmed=? where token=?"), ( 1, token))
        connection.commit()
