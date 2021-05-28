from flask import Flask
import tera

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/bot/<sentence>")
def getAnswers(sentence):
    return tera.getAnswers(sentence)