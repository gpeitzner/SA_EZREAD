from flask import Flask, request
import os
import json
import pymongo
from bson.objectid import ObjectId
from bson.json_util import dumps

app = Flask(__name__)

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
    return "<p>libro_editar</p>"


@app.route('/libros/editar', methods=['PUT'])
def actualizar():
    if request.method == 'PUT':
        content = request.get_json()
        cant = 0
        resultado = col.update_many(
            {
                "_id": ObjectId(content["id"])
            },
            {
                '$set': {
                    "Titulo": content["Titulo"],
                    "Autor": content["Autor"],
                    "Editorial": content["Editorial"],
                    "Genero": content["Genero"],
                    "Cantidad": content["Cantidad"],
                    "Activo": content["Activo"]
                }
            })
        cant = cant + resultado.modified_count

        return {"modificado": cant}


@app.route('/libros/stock', methods=['PUT'])
def descontarQuantity():
    if request.method == 'PUT':
        content = request.get_json()
        cantidadStock = 0
        cant = 0

        libro = col.find_one({'_id': ObjectId(content["id"])})

        if libro:

            cantidadStock = int(str(libro["Cantidad"]))

            if cantidadStock > 0:
                if cantidadStock > int(content["cantidad"]):

                    cantidadStock = cantidadStock - int(content["cantidad"])

                    resultado = col.update_one(
                        {
                            "_id": ObjectId(content["id"])
                        },
                        {
                            '$set': {
                                "Cantidad": cantidadStock
                            }
                        })
                    cant = cant + resultado.modified_count

                    return {"modificado": cant, "nueva Cantidad": cantidadStock}
            return {"mensaje": "Cantidad insuficiente en stock"}

        else:
            return {"mensaje": "Libro no existe"}
