from flask import Flask, request
import os
import json
import pymongo
from bson.objectid import ObjectId
from bson.json_util import dumps
from flask_cors import CORS
from bucket import Bucket
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
    return "<p>libro_editar</p>"


@app.route('/libros/editar', methods=['PUT'])
def actualizar():
    if request.method == 'PUT':
        content = request.get_json()
        cant = 0
        flag = False

        busqueda = col.find(
            {'Titulo': content['Titulo'], 'Editorial': content['Editorial'], 'Autor': content['Autor'], 'Genero': content['Genero']})

        if busqueda:
            for book in busqueda:
                if  str(book["_id"]) != content["id"]:
                    print("book-> ",book["_id"]," id-> ", content["id"])
                    flag = True
                    break

        
        if flag:
            return {"modificado": "ya existe"}
        else:
            if str(content['Imagen']).find('https://books-pics.s3.us-east-2.amazonaws.com/') == -1  :
                # hay que borrar
                
                if content["Imagen"]=="" or content["Imagen"]==" ":
                    #no le estan agregando imagen
                    content["Imagen"]= ""
                    content["Path"] = ""
                else:

                    libro = col.find_one({'_id': ObjectId(content["id"])})
                    key = libro["Path"]
                    if key:
                        s3 = Bucket()
                        s3.delete_picture(key)
                    # insertar nueva imagen
                    if str(content["Imagen"]).find('data') > -1 or str(content['Imagen']).find('base64') > -1:
                        header, base64 = content['Imagen'].split(",")
                        content['Imagen'] = base64
                    #    content["imagen"]= str(content["imagen"]).split('')
                    s3 = Bucket()

                    content['Path'] = s3.write_image(
                        content['Titulo'], content['Imagen'], '')
                    content['Imagen'] = 'https://books-pics.s3.us-east-2.amazonaws.com/' + \
                        content['Path']

            if 'Path' in content:
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
                            "Activo": content["Activo"],
                            "Imagen": content["Imagen"],
                            "Path": content["Path"],
                            "Precio": content["Precio"]
                        }
                    })
                cant = cant + resultado.modified_count
            else:
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
                            "Activo": content["Activo"],
                            "Imagen": content["Imagen"],
                            "Precio": content["Precio"]
                        }
                    })
                cant = cant + resultado.modified_count

            if cant > 0:
                now = datetime.now()
                logs.insert_one({
                    "Operacion": "Edición",
                    "Libro": content["Titulo"],
                    "Editorial": content["Editorial"],
                    "Descripcion":"Se actualizaron parametros del libro",
                    "Fecha:": '{}-{}-{} {}:{}:{}'.format(now.day, now.month, now.year, now.hour, now.minute, now.second)

                })

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
                    if cant > 0:
                        now = datetime.now()
                        logs.insert_one({
                            "Operacion": "Edición",
                            "Libro": content["Titulo"],
                            "Editorial": content["Editorial"],
                            "Descripcion":"Se actualizó el stock del libro",
                            "Fecha:": '{}-{}-{} {}:{}:{}'.format(now.day, now.month, now.year, now.hour, now.minute, now.second)

                        })

                return {"modificado": cant, "nueva Cantidad": cantidadStock}
            return {"mensaje": "Cantidad insuficiente en stock"}

        else:
            return {"mensaje": "Libro no existe"}
