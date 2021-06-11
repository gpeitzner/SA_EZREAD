from flask import Flask, request, jsonify
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


@app.route("/", methods=["POST"])
def main():
    data = request.get_json()
    email = data["email"]
    password = data["password"]
    user = col.find_one({
        'correo': email,
        'password': hashlib.sha256(password.encode()).hexdigest()
    })
    print(user)
    if user:
        user_data = {
            "_id": str(user["_id"]),
            "tipo": user["tipo"],
            "nombre": user["nombre"],
            "apellido": user["apellido"],
            "correo": user["correo"],
            "telefono": user["telefono"],
            "direccion": user["direccion"],
            "activo": user["activo"]
        }
        return jsonify(user_data)
    else:
        return jsonify({"message": "bad credentials"}), 400
