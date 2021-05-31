from os import name
from flask import Flask, json, jsonify,request
import tera
import time

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/bot/<sentence>", methods=['GET', 'POST'])
def getAnswers(sentence):
    query = dict(request.form)['query']
    return jsonify({'response':tera.getAnswers(query)}) 




if __name__ == "__main__":
    app.run(debug= False)