#coding utf8
#labo3

from flask import flask
app = Flask(__name__)

@app.route('/')
def formulaire():
    return render_template('formulaire.html')

@app.route('/envoyer', methods=['POST'])
def donnees_formulaire():
    print request.form['name']
    print request.form['fname']
    return redirect('/merci')

@app.route('/merci')
def merci():
    return render_template('merci.html')
