from flask import Flask, request
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

class Usuario:
    def __init__(self, tipo,nombre,apellido,correo,password,telefono,direccion,activo):
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
            "tipo":self.tipo,
            "nombre":self.nombre,
            "apellido":self.apellido,
            "correo": self.correo,
            "password":self.password,
            "telefono":self.telefono,
            "direccion":self.direccion,
            "activo":self.activo
        }

@app.route("/users", methods=["POST"])
def create():
    tipo = request.form.get("tipo","cliente")
    nombre = request.form["nombre"]
    apellido = request.form.get("apellido","")
    correo = request.form["correo"]
    password = request.form["password"]
    telefono = request.form.get("telefono","")
    direccion = request.form.get("direccion","")
    existe = col.find_one({'correo': correo})
    if existe:
        return {"mensaje":"Correo ya existente"}
    else:
        if tipo=="cliente":
            new_user = Usuario(tipo,nombre,apellido,correo,password,telefono,direccion,1)
        elif tipo=="administrador":
            new_user = Usuario(tipo,nombre,apellido,correo,password,telefono,direccion,1)
        else:
            new_user = Usuario(tipo,nombre,apellido,correo,password,telefono,direccion,0)
        ret = col.insert_one(new_user.toJson())
        return {"mensaje":"Usuario Insertado","id":str(ret.inserted_id)}

@app.route("/")
def main():
    return "<p>CREAR USUARIO</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True,port=5002)