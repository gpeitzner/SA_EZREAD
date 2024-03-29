from flask import Flask, request
import os
import pymongo
import hashlib
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


class Usuario:
    def __init__(self, tipo, nombre, apellido, correo, password, telefono, direccion, activo):
        self.tipo = tipo
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.password = password
        self.telefono = telefono
        self.direccion = direccion
        self.activo = activo

    def toJson(self):
        return {
            "tipo": self.tipo,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "correo": self.correo,
            "password": self.password,
            "telefono": self.telefono,
            "direccion": self.direccion,
            "activo": self.activo
        }


def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature


@app.route("/users", methods=["POST"])
def create():
    data = request.get_json()
    tipo = data.get("tipo", "cliente")
    nombre = data["nombre"]
    apellido = data.get("apellido", "")
    correo = data["correo"]
    password = data["password"]
    telefono = data.get("telefono", "")
    direccion = data.get("direccion", "")
    existe = col.find_one({'correo': correo})
    sha_signature = encrypt_string(password)
    print(sha_signature)
    if existe:
        return {"mensaje": "Correo ya existente"}
    else:
        if tipo == "cliente":
            new_user = Usuario(tipo, nombre, apellido, correo,
                               sha_signature, telefono, direccion, 1)
        elif tipo == "administrador":
            new_user = Usuario(tipo, nombre, apellido, correo,
                               sha_signature, telefono, direccion, 1)
        else:
            new_user = Usuario(tipo, nombre, apellido, correo,
                               sha_signature, telefono, direccion, 0)
        ret = col.insert_one(new_user.toJson())
        return {"mensaje": "Usuario Insertado", "id": str(ret.inserted_id)}


@app.route("/")
def main():
    return "<p>CREAR USUARIO</p>"
