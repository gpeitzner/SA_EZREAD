from flask import Flask, request
import os
import json
import pymongo
from bson.objectid import ObjectId
from bson.json_util import dumps
from flask_cors import CORS
from datetime import datetime

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
logs = db["logs"]


@app.route("/")
def main():
    return "<p>libro_eliminar</p>"


@app.route('/libros/eliminar', methods=['DELETE'])
def actualizar():
    if request.method == 'DELETE':
        idDoc = request.args.get("id")
        cant = 0
        libro = col.find_one({'_id': ObjectId(idDoc)})

        if libro:
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

            if cant > 0:
                now = datetime.now()
                logs.insert_one({
                    "Operacion": "Eliminación",
                    "Libro": libro["Titulo"],
                    "Editorial": libro["Editorial"],
                    "Descripcion": "Se elimino el libro de stock",
                    "Fecha:": '{}-{}-{} {}:{}:{}'.format(now.day, now.month, now.year, now.hour, now.minute, now.second)

                })
            # 0--> no hubo cambios 1--> cambio de estado 1 a 0
            return {"eliminado": cant}
        else:
            return {"eliminado": 0}
