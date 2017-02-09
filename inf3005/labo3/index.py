#coding: utf8
#labo3

from flask import Flask
from flask import render_template
from flask import redirect
from flask import request

app = Flask(__name__)

@app.route('/')
def formulaire():
    return render_template('formulaire.html')

@app.route('/envoyer', methods=['POST'])
def donnees_formulaire():
    if request.form['name'] == "" or request.form['fname'] == "":
        return redirect('/erreur')
    else:
        print request.form['name']
        print request.form['fname']
        return redirect('/merci')

@app.route('/erreur')
def erreur():
    return render_template('erreur.html')

@app.route('/merci')
def merci():
    return render_template('merci.html')
