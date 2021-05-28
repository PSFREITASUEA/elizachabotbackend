from flask import Flask

from tera import Tera

app = Flask(__name__)
tera = Tera()

@app.route("/")
def index():
    return "Hello World!"

@app.route("/bot/<sentence>")
def getAnswers(sentence):
    return tera.getAnswers(tera,sentence)