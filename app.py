from os import name
import os
from flask import Flask, json, jsonify,request
import tera
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
def index():
    return "Hello World!"

@app.route("/bot2/<sentence>", methods=['GET', 'POST'])
def getAnswers(sentence):
    query = dict(request.form)['query']
    return jsonify({'response':tera.getAnswers(query)}) 

@cross_origin
@app.route("/bot/<sentence>")
def getAnotherAnwsers(sentence):
    return jsonify({'response':tera.getAnswers(sentence)}) 

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)