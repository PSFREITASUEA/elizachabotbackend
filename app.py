from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/bot/<sentence>")
def getAnswers(sentence):
    return "Olá, sou o Tera.py!!! Como posso ajudá-lo," + str(sentence)+ "?"