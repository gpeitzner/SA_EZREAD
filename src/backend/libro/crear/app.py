from flask import Flask, request
import os
import json
import pymongo
from bucket import Bucket
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
            # insertar imagen viene en content['image']

            if (content["Imagen"]):
                if str(content["Imagen"]).find('data') > -1 or str(content['Imagen']).find('base64') > -1:
                    header, base64 = content['Imagen'].split(",")
                    content['Imagen'] = base64

            #    content["imagen"]= str(content["imagen"]).split('')
                s3 = Bucket()

                content['Path'] = s3.write_image(
                    content['Titulo'], content['Imagen'], '')
                content['Imagen'] = 'https://ezreadbooks.s3.us-east-2.amazonaws.com/'+content['Path']
            else:
                content["Path"] = ""
                content["Imagen"] = ""
            # insertar nuevo objeto con imagen

            if 'Imagen' in content and 'Path' in content and 'Precio' in content and 'Autor' in content and 'Titulo' in content and 'Editorial' in content and 'Genero' in content and 'Activo' in content and 'Cantidad' in content:
                ret = col.insert_one(content)

                if ret:
                    now = datetime.now()
                    logs.insert_one({
                        "Operacion": "Creacion",
                        "Libro": content["Titulo"],
                        "Editorial": content["Editorial"],
                        "Descripcion": "Se registró el libro en la base de datos",
                        "Fecha:": '{}-{}-{} {}:{}:{}'.format(now.day, now.month, now.year, now.hour, now.minute, now.second)

                    })
                    return {"mensaje": "insertado", "id": str(ret.inserted_id)}
                else:
                    {"mensaje": "error"}
            else:
                return {"mensaje": "faltan campos"}
