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
def main2():
    return "<p>libro_obtener</p>"


@app.route("/libros")  # obbtener todos los libros registrados.
def main():
    if request.method == 'GET':
        busqueda = col.find()

        if busqueda:
            libros = []
            for libro in busqueda:

                if (libro['Activo']):
                    libros.append({"id": str(libro['_id']), "Titulo": str(libro['Titulo']), "Editorial": str(
                        libro['Editorial']), "Autor": str(libro['Autor']), "Genero": str(libro['Genero']),
                        "Cantidad": libro['Cantidad'], "Activo": libro['Activo'], "Precio": libro['Precio'],
                        "Imagen": libro['Imagen']})

            return {'libros': libros}
        else:
            return {"libros": []}


@app.route('/libro', methods=['GET'])  # por medio de id
def obtenerLibro():
    if request.method == 'GET':
        content = request.args.get('id')
        libro = col.find_one({'_id': ObjectId(content)})

        if libro:

            if (libro['Activo']):
                return {'libro': {"id": str(libro['_id']), "Titulo": str(libro['Titulo']), "Editorial": str(
                        libro['Editorial']), "Autor": str(libro['Autor']), "Genero": str(libro['Genero']),
                    "Cantidad": libro['Cantidad'], "Activo": libro['Activo'], "Precio": libro['Precio'],
                        "Imagen": libro['Imagen']}}
            else:
                return {"mensaje": "Libro fuera de stock"}

        else:
            return {"mensaje": "Libro no existe"}


# traer todos los generos con sus libros
@app.route('/libros/Generos', methods=['GET'])
def obtenerGeneros():
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
                                'Autor': "$Autor",
                                'Cantidad': "$Cantidad",
                                'Activo': "$Activo",
                                'Precio': "$Precio",
                                'Imagen': "$Imagen"
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
                    if (libro['Activo']):
                        books.append({"id": str(libro['id']), "Titulo": str(libro['Titulo']), "Editorial": str(
                            libro['Editorial']), "Autor": str(libro['Autor']),
                            "Cantidad": libro['Cantidad'], "Activo": libro['Activo'], "Precio": libro['Precio'],
                            "Imagen": libro['Imagen']})

                list2.append({'Genero': genero['_id'], 'libros': books})
            return {'Generos': list2}
        else:
            return {'Generos': []}


# traer todos las editoriales con sus libros
@app.route('/libros/Editoriales', methods=['GET'])
def obtenerEditoriales():
    if request.method == 'GET':
        ret = col.aggregate([
            {'$group': {
                '_id': "$Editorial",
                'libros': {'$push':
                            {
                                'id': '$_id',
                                'Editorial': "$Editorial",
                                'Titulo': "$Titulo",
                                'Genero': "$Genero",
                                'Autor': "$Autor",
                                'Cantidad': "$Cantidad",
                                'Activo': "$Activo",
                                'Imagen' : "$Imagen",
                                'Precio': "$Precio"
                            },
                            }
            }
            }
        ])
        if ret:

            l = list(ret)
            list2 = []
            for editorial in l:
                books = []
                for libro in editorial['libros']:
                    if (libro['Activo']):
                        books.append({"id": str(libro['id']), "Titulo": str(libro['Titulo']), "Genero": str(
                            libro['Genero']), "Autor": str(libro['Autor']),
                            "Cantidad": libro['Cantidad'],  "Activo": libro['Activo'], "Precio": libro['Precio'],
                            "Imagen": libro['Imagen']})

                list2.append({'Editorial': editorial['_id'], 'libros': books})
            return {'Editoriales': list2}
        else:
            return {'Editoriales': []}


# obtener libros de una editorial en específico
@app.route('/libros/byEditorial', methods=['GET'])
def obtenerbyEditorial():
    if request.method == 'GET':
        editorial = request.args.get('user')
        ret = col.aggregate([
            {
                '$match': {'Editorial': editorial}
            }
        ])

        if ret:
            l = list(ret)
            books = []
            for libro in l:
                if (libro['Activo']):
                    books.append({"id": str(libro['_id']), "Titulo": str(libro['Titulo']), "Genero": str(
                        libro['Genero']), "Autor": str(libro['Autor']),
                        "Cantidad": libro['Cantidad'], "Activo": libro['Activo'], "Precio": libro['Precio'],
                        "Imagen": libro['Imagen']})
            return {'libros': books}
        else:
            return {'libros': []}
