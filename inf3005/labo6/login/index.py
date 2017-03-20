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

from flask import Flask
from flask import render_template
from flask import g
from flask import request
from flask import redirect
from flask import session
from flask import Response
from database import Database
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import hashlib
import uuid
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


@app.route('/')
def start_page():
    username = None
    prenom = None
    nom = None
    confirmed = None
    if "id" in session:
        username = get_db().get_session(session["id"])
        rs = get_db().get_name_fname_confirmed(username)
        if rs is not None:
            prenom = rs[0]
            nom = rs[1]
            confirmed = rs[2]
            print confirmed

    return render_template('accueil.html', prenom=prenom, nom=nom, confirmed=confirmed)


@app.route('/confirmation')
def confirmation_page():
    return render_template('confirmation.html')


@app.route('/formulaire', methods=["GET", "POST"])
def formulaire_creation():
    if request.method == "GET":
        return render_template("formulaire.html")
    else:
        username = request.form["username"]
        prenom = request.form["prenom"]
        nom = request.form["nom"]
        password = request.form["password"]
        email = request.form["email"]
        # Vérifier que les champs ne sont pas vides
        if username == "" or password == "" or email == "" or prenom == "" or nom == "":
            return render_template("formulaire.html",
                                   error="Tous les champs sont obligatoires.")

        # TODO Faire la validation du formulaire
        salt = uuid.uuid4().hex
        hashed_password = hashlib.sha512(password + salt).hexdigest()
        db = get_db()
        db.create_user(username, prenom, nom, email, salt, hashed_password)

        token = uuid.uuid4().hex
        db.set_token(token,username)
        source_address = "inf3005@gmail.com"
        destination_address = email
        body = ("""Veuillez cliquez sur ce lien pour confirmer votre addresse courriel.
                                http://localhost:5000/activation/%s""" % token)
        subject = "Confirmation email"

        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = source_address
        msg['To'] = destination_address

        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(source_address, "secret123")
        text = msg.as_string()
        server.sendmail(source_address, destination_address, text)
        server.quit()
        return redirect("/confirmation")


@app.route('/login', methods=["POST"])
def log_user():
    username = request.form["username"]
    password = request.form["password"]
    # Vérifier que les champs ne sont pas vides
    if username == "" or password == "":
        return redirect("/")

    user = get_db().get_user_login_info(username)
    if user is None:
        return redirect("/")

    salt = user[0]
    hashed_password = hashlib.sha512(password + salt).hexdigest()
    if hashed_password == user[1]:
        # Accès autorisé
        id_session = uuid.uuid4().hex
        get_db().save_session(id_session, username)
        session["id"] = id_session
        return redirect("/")
    else:
        return redirect("/")


@app.route('/activation/<jeton>')
def activation_email(jeton):
    token = get_db().get_token(jeton)
    if token is None:
        return render_template('404.html'), 404
    else:
        get_db().set_confirmation_email(token)
        return redirect("/")

def authentication_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not is_authenticated(session):
            return send_unauthorized()
        return f(*args, **kwargs)
    return decorated


@app.route('/logout')
@authentication_required
def logout():
    if "id" in session:
        id_session = session["id"]
        session.pop('id', None)
        get_db().delete_session(id_session)
    return redirect("/")


def is_authenticated(session):
    return "id" in session


def send_unauthorized():
    return Response('Could not verify your access level for that URL.\n'
                    'You have to login with proper credentials', 401,
                    {'WWW-Authenticate': 'Basic realm="Login Required"'})


app.secret_key = "(*&*&322387he738220)(*(*22347657"
