from flask import Flask, request
import os
import json
import pymongo
from bson.objectid import ObjectId
from bson.json_util import dumps
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

db_host = os.environ["db_host"] if "db_host" in os.environ else "localhost"
db_password = os.environ["db_password"] if "db_password" in os.environ else ""
db_port = int(os.environ["db_port"]) if "db_port" in os.environ else 27017
db_name = os.environ["db_name"] if "db_name" in os.environ else "ezread"
db_user = os.environ["db_user"] if "db_user" in os.environ else ""

client = pymongo.MongoClient(
    host=db_host, port=db_port, username=db_user, password=db_password)
db = client[str(db_name)]
col = db["libros"]


@app.route("/")
def main():
    return "<p>libro_eliminar</p>"


@app.route('/libros/eliminar', methods=['DELETE'])
def actualizar():
    if request.method == 'DELETE':
        idDoc = request.args.get("id")
        cant = 0
        resultado = col.update_one(
            {
                "_id": ObjectId(idDoc)
            },
            {
                '$set': {
                    "Activo": 0
                }
            })
        cant = cant + resultado.modified_count

        return {"eliminado": cant} # 0--> no hubo cambios 1--> cambio de estado 1 a 0 
