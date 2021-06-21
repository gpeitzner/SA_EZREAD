import os
import time
import json
from werkzeug.utils import secure_filename, send_file
from bson import ObjectId
from flask import Flask, request, jsonify
import pymongo
from flask_cors import CORS
import boto3


app = Flask(__name__)
CORS(app)


db_host = os.environ["db_host"] if "db_host" in os.environ else "localhost"
db_password = os.environ["db_password"] if "db_password" in os.environ else ""
db_port = int(os.environ["db_port"]) if "db_port" in os.environ else 27017
db_name = os.environ["db_name"] if "db_name" in os.environ else "ezread"
db_user = os.environ["db_user"] if "db_user" in os.environ else ""


s3_bucket_name = os.environ["s3_bucket_name"] if "s3_bucket_name" in os.environ else ""
s3_region_name = os.environ["s3_region_name"] if "s3_region_name" in os.environ else ""
s3_access_key_id = os.environ["s3_access_key_id"] if "s3_access_key_id" in os.environ else ""
s3_access_key = os.environ["s3_access_key"] if "s3_access_key" in os.environ else ""


s3 = boto3.client(
    "s3",
    region_name=s3_region_name,
    aws_access_key_id=s3_access_key_id,
    aws_secret_access_key=s3_access_key
)


client = pymongo.MongoClient(
    host=db_host,
    port=db_port,
    username=db_user,
    password=db_password
)
db = client[str(db_name)]
col = db["solicitudes"]


@app.route("/solicitud", methods=["GET"])
def read():
    id = request.args.get("id")
    if id:
        data = col.find_one({
            '_id': ObjectId(str(id))
        })
        result = {
            "id": str(data["_id"]),
            "nombre": data["nombre"],
            "autor": data["autor"],
            "fecha": data["fecha"],
            "url": data["url"]
        }
        return jsonify(result)
    book_requests = col.find()
    result = []
    for book_request in book_requests:
        result.append({
            "id": str(book_request["_id"]),
            "nombre": book_request["nombre"],
            "autor": book_request["autor"],
            "fecha": book_request["fecha"],
            "url": book_request["url"]
        })
    return jsonify(result)


@app.route("/solicitud", methods=["POST"])
def create():
    data = request.get_json()
    book_name = data["nombre"]
    book_autor = data["autor"]
    book_date = data["fecha"]
    book_url = data["url"]
    new_book_request = col.insert_one(data)
    return jsonify({
        "id": str(new_book_request.inserted_id),
        "nombre": book_name,
        "autor": book_autor,
        "fecha": book_date,
        "url": book_url
    })


@app.route("/solicitud/subir", methods=["POST"])
def upload():
    new_file = request.files["file"]
    if new_file:
        sanitized_filename = secure_filename(new_file.filename)
        filename = str(time.time()).replace(".", "")
        file_extension = sanitized_filename.split(".")[1]
        final_name = filename + "." + file_extension
        new_file.save(final_name)
        s3.upload_file(
            Bucket=s3_bucket_name,
            Filename=final_name,
            Key=final_name,
            ExtraArgs={'ACL': 'public-read'}
        )
        os.remove(final_name)
        final_url = "https://" + s3_bucket_name + ".s3." + \
            s3_region_name + ".amazonaws.com/"+final_name
        return jsonify({"url": final_url})
    else:
        return jsonify({"message": "not file sended"}), 400


@app.route("/solicitud", methods=["DELETE"])
def delete():
    id = request.args.get("id")
    if id:
        col.delete_one({
            '_id': ObjectId(str(id))
        })
        return jsonify({"message": "book request deleted"})
    return jsonify({"message": "empty id"}), 400


@app.route("/impuesto", methods=["GET"])
def taxes():
    taxes = json.loads(open("taxes.json", "r").read())
    return jsonify(taxes)
