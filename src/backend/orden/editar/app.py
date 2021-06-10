from flask import Flask, request
from bson.objectid import ObjectId
import os
import pymongo
import json
#EDITAR
app = Flask(__name__)

db_host = os.environ["db_host"] if "db_host" in os.environ else "localhost"
db_password = os.environ["db_password"] if "db_password" in os.environ else ""
db_port = int(os.environ["db_port"]) if "db_port" in os.environ else 27017
db_name = os.environ["db_name"] if "db_name" in os.environ else "ezread"

client = pymongo.MongoClient(db_host, db_port)
db = client[str(db_name)]
col = db["ordenes"]

@app.route("/ordenes", methods=["PUT"])
def create():
    usuario = request.form["usuario"]
    estado = request.form.get("estado","0")
    libros = json.loads(request.form["libros"])
    existe = col.find_one({'usuario': usuario, 'estado':"0"})
    if existe:
        Qid = ObjectId(existe['_id'])
        myquery = { "_id": Qid }
        newvalues = { "$set": {"usuario":usuario,"estado":estado,"libros":libros} }
        col.update_one(myquery,newvalues)  
        return {"mensaje":"Orden modificada"}
    else:
        return {"mensaje":"El usuario no tiene orden activa"}
#[{"id_libro":"321","cantidad_libro":"1","precio_libro":"10"}]
@app.route("/")
def main():
    return "<p>orden_editar</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True,port=5002)