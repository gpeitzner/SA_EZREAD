from flask import Flask, redirect, url_for, render_template, request
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

class Usuario:
    def __init__(self,nombre,apellido,correo,password,telefono,direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.password = password
        self.telefono = telefono
        self.direccion = direccion
    
    def toJson(self):
        return {
            "nombre":self.nombre,
            "apellido":self.apellido,
            "correo": self.correo,
            "password":self.password,
            "telefono":self.telefono,
            "direccion":self.direccion,
        }
    def toJsonWithoutPass(self):
        return {
            "nombre":self.nombre,
            "apellido":self.apellido,
            "correo": self.correo,
            "telefono":self.telefono,
            "direccion":self.direccion,
        }

@app.route("/users", methods=["POST"])
def edit():
    id = request.form["id"]
    nombre = request.form["nombre"]
    apellido = request.form.get("apellido","")
    correo = request.form["correo"]
    password = request.form.get("password","")
    telefono = request.form.get("telefono","")
    direccion = request.form.get("direccion","")
    new_user = Usuario(nombre,apellido,correo,password,telefono,direccion)
    
    Qid = ObjectId(id)
    myquery = { "_id": Qid }
    if password == "":
        newvalues = { "$set": new_user.toJson() }    
    else:
        newvalues = { "$set": new_user.toJsonWithoutPass() }
    
    col.update_one(myquery,newvalues)
    return {"mensaje":"Modificado"}

@app.route("/")
def main():
    return "<p>EDITAR USUARIO</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True,port=5003)  
