from flask import Flask
from flask import render_template
from flask import g
from flask import request
from flask import redirect
from database import Database
import re
import hashlib
import uuid

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


@app.route('/')
def page_acceuil():
    return render_template('form.html')


@app.route('/envoyer', methods=['POST'])
def page_envoyer():
    nom = request.form['nom']
    prenom = request.form['prenom']
    courriel = request.form['courriel']
    courrielconf = request.form['courrielconf']
    motdepasse = request.form['motdepasse']

    if len(nom) == 0 or len(prenom) == 0 or len(courriel) == 0 or courriel != courrielconf or len(motdepasse) == 0:
        return render_template('form.html')

    if len(motdepasse) < 8:
        err_mdp = "Le mot de passe doit contenir au moins 8 caractere."
    elif not re.search(r"\d", motdepasse):
        err_mdp = "Le mot de passe doit contenir un chiffre."
    elif not re.search(r"[A-Z]", motdepasse):
        err_mdp = "Le mot de passe doit contenir au moins une majuscule."
    elif not re.search(r"[a-z]", motdepasse):
        err_mdp = "Le mot de passe doit contenir au moins une minuscule."
    elif not re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~"+r'"]', motdepasse):
        err_mdp = "Le mot de passe doit contenir au moins 1 symbole."
    else:
        err_mdp = ""

    if len(err_mdp) != 0:
        return render_template('form.html', err_mdp=err_mdp)

    salt = uuid.uuid4().hex
    hashed = hashlib.sha512(motdepasse + salt).hexdigest()
    user = [nom, prenom, courriel, salt, hashed]
    get_db().insert_user(user)

    return render_template('merci.html')
