from flask import Flask, request
from bson.objectid import ObjectId
import os
import pymongo
from flask_cors import CORS
import json
#CREAR
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
col = db["ordenes"]
class Orden:
    def __init__(self, id_user,estado,libros, pago, envio):
        self.id_user = id_user
        self.estado = estado
        self.libros = libros
        self.pago = pago
        self.envio = envio
    
    def toJson(self):
        return {
            "usuario":self.id_user,
            "estado":self.estado,
            "libros":self.libros,
            "tipoPago":self.pago,
            "tipoEnvio":self.envio
        }

@app.route("/ordenes", methods=["POST"])
def create():
    data = request.get_json()
    usuario = data["usuario"]
    estado = data.get("estado","0")
    #libros = json.loads(request.form["libros"])
    libros = data["libros"]
    pago = data["tipoPago"]
    envio = data["tipoEnvio"]
    existe = col.find_one({'usuario': usuario, 'estado':"0"})
    if existe: #Se modifica
        #print(existe['usuario'])
        #return {"mensaje":existe['usuario']}
        #--existe['libros'].append({"id_libro":libro,"cantidad_libro":cantidad,"precio_libro":precio})
        #--Qid = ObjectId(existe['_id'])
        #--myquery = { "_id": Qid }
        #--newvalues = { "$set": {"usuario":existe["usuario"],"estado":existe['estado'],"libros":existe['libros']} }
        #newvalues = { "$set": existe.toJson() }
        #--col.update_one(myquery,newvalues)  
        return {"mensaje":"Ya tiene una orden en proceso"}
    else: #Se crea
        nuevaorden = Orden(usuario,estado,libros,pago,envio)
        ret = col.insert_one(nuevaorden.toJson())
        return {"mensaje":"Orden creada","id":str(ret.inserted_id)}
@app.route("/")
def main():
    return "<p>orden_crear</p>"

#if __name__ == "__main__":
    #app.run(host="0.0.0.0",debug=True,port=5010)