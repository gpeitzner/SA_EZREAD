from flask import Flask, request
from bson.objectid import ObjectId
import os
import pymongo
#OBTENER
app = Flask(__name__)

db_host = os.environ["db_host"] if "db_host" in os.environ else "localhost"
db_password = os.environ["db_password"] if "db_password" in os.environ else ""
db_port = int(os.environ["db_port"]) if "db_port" in os.environ else 27017
db_name = os.environ["db_name"] if "db_name" in os.environ else "ezread"

client = pymongo.MongoClient(db_host, db_port)
db = client[str(db_name)]
col = db["ordenes"]

@app.route("/ordenes", methods=["GET"])
def create():
    usuario = request.form["usuario"]
    existe = col.find_one({'usuario': usuario, 'estado':"0"})
    if existe: #se retorna
        #print(existe['usuario'])
        return {"usuario":existe['usuario'],"estado":existe['estado'],"libros":existe['libros']}
    else: #no existe
        return {"mensaje":"No tiene ordenes"}
@app.route("/")
def main():
    return "<p>orden_obtener</p>"
if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True,port=5005)