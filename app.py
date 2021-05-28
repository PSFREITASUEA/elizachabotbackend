from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/bot")
def getAnswers():
    return "Esta é uma resposta do bot!!"