from flask import Flask
from bson.objectid import ObjectId
import os
import pymongo
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
col = db["usuarios"]


@app.route("/users")
def obtener():
    users = []
    for user in col.find():
        if str(user['tipo']!="administrador"):
            users.append({"id": str(user['_id']), "nombre": str(user['nombre']), "apellido": str(
                user['apellido']), "correo": str(user['correo']), "telefono": str(user['telefono']), "direccion": str(user['direccion']), "tipo": str(user['tipo']), "activo": str(user['activo'])})
    return {'users': users}


@app.route("/users/<string:id>")
def obtenerUser(id):
    user = col.find_one({'_id': ObjectId(id)})
    if user:
        return{"id": str(user['_id']), "nombre": str(user['nombre']), "apellido": str(
            user['apellido']), "correo": str(user['correo']), "telefono": str(user['telefono']), "direccion": str(user['direccion']), "tipo": str(user['tipo']), "activo": str(user['activo'])}
    else:
        return {"mensaje": "Usuario no existe"}


@app.route("/")
def main():
    return "<p>OBTENER USUARIOS</p>"
