from flask import Flask, render_template, request
import json

app = Flask(__name__)

file = open("terms.json", encoding="utf-8")
db = json.load(file)

@app.route("/")
def home():
    return render_template("welcome.html", title="Welcome!")

@app.route("/dicionario")
def dicionario_medico():
    return render_template('dicionario_medico.html')

@app.route("/terms")
def terms():
    return render_template('terms.html', designations=db.keys())

@app.route("/term/<t>")
def term(t):
    return render_template('term.html', designation=t, value=db.get(t,"None"))

app.run(host="localhost", port=3000, debug=True)

