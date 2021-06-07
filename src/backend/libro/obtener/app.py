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

client = pymongo.MongoClient(db_host, db_port)
db = client[str(db_name)]
col = db["libros"]


@app.route("/")
def main():
    if request.method == 'GET':
        busqueda = col.find()

        if busqueda:
            libros = []
            for libro in busqueda:
                libros.append({"id": str(libro['_id']), "Titulo": str(libro['Titulo']), "Editorial": str(
                    libro['Editorial']), "Autor": str(libro['Autor']), "Genero": str(libro['Genero'])})

            return {'libros': libros}
        else:
            return {"libros": []}


@app.route('/libro', methods=['GET'])  # por medio de titulo
def obtenerLibro():
    if request.method == 'GET':
        content = request.args.get('id')
        libro = col.find_one({'_id': ObjectId(content)})

        if libro:

            return {'libro': {"id": str(libro['_id']), "Titulo": str(libro['Titulo']), "Editorial": str(
                    libro['Editorial']), "Autor": str(libro['Autor']), "Genero": str(libro['Genero'])}}
        else:
            return {"mensaje": "Libro no existe"}


@app.route('/Genero', methods=['GET'])  # por medio de titulo
def obtenerByGenders():
    if request.method == 'GET':
        ret = col.aggregate([
            {'$group': {
                '_id': "$Genero",
                'libros': {'$push':
                            {
                                'id': '$_id',
                                'Editorial': "$Editorial",
                                'Titulo': "$Titulo",
                                'Genero': "$Genero",
                                'Autor': "$Autor"
                            },
                            }
            }
            }
        ])

        if ret:

            l = list(ret)
            list2 = []
            for genero in l:
                books = []
                for libro in genero['libros']:
                    books.append({"id": str(libro['id']), "Titulo": str(libro['Titulo']), "Editorial": str(
                        libro['Editorial']), "Autor": str(libro['Autor'])})

                list2.append({'Genero': genero['_id'], 'libros': books})
            return {'Generos': list2}
        else:
            return {'Generos': []}
