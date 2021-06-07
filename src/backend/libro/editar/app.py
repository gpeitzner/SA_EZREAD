from flask import Flask, request
import os
import pymongo
import json

app = Flask(__name__)

db_host = os.environ["db_host"] if "db_host" in os.environ else "localhost"
db_password = os.environ["db_password"] if "db_password" in os.environ else ""
db_port = int(os.environ["db_port"]) if "db_port" in os.environ else 27017
db_name = os.environ["db_name"] if "db_name" in os.environ else "ezread"

client = pymongo.MongoClient(db_host, db_port)
db = client[str(db_name)]
col = db["libros"]


@app.route("/")
def main():
    return "<p>libro_editar</p>"


@app.route('/', methods=['PUT'])
def actualizar():
    if request.method == 'PUT':
        content = request.get_json()
        resultado = col.update_many(
            {
                "_id": content['id']
            },
            {
                '$set': {
                    "Titulo": content["Titulo"]
                }
            })
        cant = cant + resultado.modified_count

        return {"modificado": str(cant)}
