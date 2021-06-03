from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>login</p>" + str(os.environ["db_host"])