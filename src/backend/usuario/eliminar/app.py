from flask import Flask, redirect, url_for, render_template, request
from bson.objectid import ObjectId
import os
import pymongo

app = Flask(__name__)

db_host = os.environ["db_host"] if "db_host" in os.environ else "localhost"
db_password = os.environ["db_password"] if "db_password" in os.environ else ""
db_port = int(os.environ["db_port"]) if "db_port" in os.environ else 27017
db_name = os.environ["db_name"] if "db_name" in os.environ else "ezread"
db_user = os.environ["db_user"] if "db_user" in os.environ else ""

client = pymongo.MongoClient(
    host=db_host, port=db_port, username=db_user, password=db_password)
db = client[str(db_name)]
col = db["usuarios"]


@app.route("/users/<string:id>", methods=["DELETE"])
def remove(id):
    Qid = ObjectId(id)
    myquery = {"_id": Qid}
    col.delete_one(myquery)
    return {"mensaje": "Eliminado"}


@app.route("/")
def main():
    return "<p>ELIMINAR USUARIO</p>"
