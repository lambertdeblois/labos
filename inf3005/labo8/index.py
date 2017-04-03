from flask import Flask
from flask import render_template
from flask import g
from flask import request
from flask import redirect
from flask import session
from flask import Response
from flask import jsonify
from database import Database
import hashlib
import uuid
import re
from functools import wraps


app = Flask(__name__)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        g._database = Database()
    return g._database


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.disconnect()


@app.route('/api/livres', methods=['GET'])
def livres():
    if request.method == "GET":
        livres = get_db().get_livres()
        data = [{"_id": each[0], "titre": each[1]} for each in livres]
        return jsonify(data)

@app.route('/api/livre/<identifiant>', methods=['GET', 'DELETE'])
def livre(identifiant):
    if request.method == 'GET':
        livre = get_db().get_livre(identifiant)
        data = {"_id": livre[0], "titre": livre[1], "auteur": livre[2],
                "annee_pub": livre[3], "nb_pages": livre[4], "nb_chapitres": livre[5]}
        return jsonify(data)
    if request.method == 'DELETE':
        get_db().delete_livre(identifiant)
        return ""

@app.route('/api/livre', methods=['POST'])
def nouveau_livre():
    if request.method == 'POST':
        data = request.get_json()
        return "", 201
