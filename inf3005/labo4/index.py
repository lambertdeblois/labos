#coding: utf8
#labo4

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
    errname = ""
    errfname = ""
    name = request.form['name']
    fname = request.form['fname']
    if name == "":
        errname = "le nom est obligatoire"
    elif fname == "":
        errfname = "le prenom est obligatoire"

    else:
        return redirect('/merci')

    print name, fname
    return render_template('formulaire.html', errname=errname, errfname=errfname, name=name, fname=fname)


#faire classe personnes avec nom/prenom/age
@app.route('/liste')
def liste():
    cursor = conn.cursor()
    cursor.execute("selectr * from Personne")

    personnes = []
    for row in cursor:
        p = Personne(row[1], row[2], [3])
        personnes.append(p)



@app.route('/merci')
def merci():
    return render_template('merci.html')
