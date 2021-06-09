from flask import Flask, request
import os
import json
import pymongo

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
    return "<p>libro_crear</p>"


@app.route('/libros/crear', methods=['POST'])
def save():
    if request.method == 'POST':
        content = request.get_json()
        busqueda = col.find_one(
            {'Titulo': content['Titulo'], 'Editorial': content['Editorial'], 'Autor': content['Autor'], 'Genero': content['Genero']})

        if busqueda:
            return {"mensaje": "ya existe"}
        else:
            ret = col.insert_one(content)
            return {"mensaje": "insertado", "id": str(ret.inserted_id)}
