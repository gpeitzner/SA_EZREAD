from flask import Flask
from bson.objectid import ObjectId
import os
import pymongo

app = Flask(__name__)

db_host = os.environ["db_host"] if "db_host" in os.environ else "localhost"
db_password = os.environ["db_password"] if "db_password" in os.environ else ""
db_port = int(os.environ["db_port"]) if "db_port" in os.environ else 27017
db_name = os.environ["db_name"] if "db_name" in os.environ else "ezread"

client = pymongo.MongoClient(db_host, db_port)
db = client[str(db_name)]
col = db["usuarios"]

@app.route("/users")
def obtener():
    users = []
    for user in col.find():
        users.append({"id": str(user['_id']), "nombre": str(user['nombre']), "apellido": str(
                    user['apellido']), "correo": str(user['correo']), "telefono": str(user['telefono']),"direccion": str(user['direccion']),"tipo": str(user['tipo'])})
    return {'users':users}

@app.route("/users/<string:id>")
def obtenerUser(id):
    user = col.find_one({'_id': ObjectId(id)})
    if user:
        return{"id": str(user['_id']), "nombre": str(user['nombre']), "apellido": str(
                        user['apellido']), "correo": str(user['correo']), "telefono": str(user['telefono']),"direccion": str(user['direccion']),"tipo": str(user['tipo'])}
    else:
        return {"mensaje":"Usuario no existe"}

@app.route("/")
def main():
    return "<p>OBTENER USUARIOS</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True,port=5005)  