from flask import Flask

from tera import Tera

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/bot/<sentence>")
def getAnswers(sentence):
    return Tera.getAnswers(sentence)