from flask import Flask, jsonify,request
import os
import time


app = Flask(__name__)
@app.route("/bot",method=["POST"])

@app.route('/')
def index():
    return "<h1> Deployed to Heroku</h1>"

#response
def response():
    query = dict(request.form)["query"]
    result = query + " " + time.ctime()
    return jsonify({"response" : result})


@app.route("/")
def index():
    return "<h1>Hello World</hi>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)