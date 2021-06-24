from flask import Flask, request
import os
import pymongo
from flask_cors import CORS
import smtplib
from datetime import datetime, date
from pyinvoice.models import InvoiceInfo, ServiceProviderInfo, ClientInfo, Item
from pyinvoice.templates import SimpleInvoice
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
    nombreUsuario=data["nombreUsuario"]
    correoUsuario=data["correoUsuario"]
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
        crearfactura(nombreUsuario,correoUsuario,libros)
        enviarFactura(mensaje="Se genero la nueva factura y se envio",correo_destino=correoUsuario)
        return {"mensaje":"Orden creada","id":str(ret.inserted_id)}

@app.route("/factura", methods=["GET"])
def getFactura():
    #CODIGO PARA GENERAR factura en pdf
    libros=  [{ 'id': "123123", 'cantidad': "1", 'precio': "123"},{ 'id': "456456", 'cantidad': "3", 'precio':"456"}]
    crearfactura("Juan perez","esthuardo12@gmail.com",libros)
    enviarFactura(mensaje="Se genero la nueva factura y se envio",correo_destino="esthuardo12@gmail.com")
    return {"mensaje":"Proceso terminado"}

def enviarFactura(mensaje,correo_destino):
    #import email
    from email.mime.application import MIMEApplication
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    
    server.login('ezreadcorp@gmail.com', 'ezread123')
    msg = MIMEMultipart()

    message = mensaje
    msg['Subject'] = "Factura de Compra EZREAD"
    msg['From'] = 'ezreadcorp@gmail.com'
    msg['To'] = correo_destino
    msg.attach(MIMEText(message, "plain"))
    with open("./factura.pdf", "rb") as f:
        attach = MIMEApplication(f.read(),_subtype="pdf")
    attach.add_header('Content-Disposition','attachment',filename=str("FacturaElectronica.pdf"))
    msg.attach(attach)
    server.send_message(msg)

def crearfactura(nombre, correo, libros):
    doc = SimpleInvoice('factura.pdf')
    # Paid stamp, optional
    doc.is_paid = True
    doc.invoice_info = InvoiceInfo(1023, datetime.now(), datetime.now())  # Invoice info, optional
    # Service Provider Info, optional
    doc.service_provider_info = ServiceProviderInfo(
        name=nombre,
        street='Guatemala',
        city='Guatemala',
        post_code='222222',
        vat_tax_number='7555605-7'
    )
    # Client info, optional
    doc.client_info = ClientInfo(email=correo)
    # Add Item
    for x in libros:
        doc.add_item(Item(x['id'], x['id'], x['cantidad'], x['precio']))
    # Tax rate, optional
    #doc.set_item_tax_rate(0)  # 20%
    # Transactions detail, optional
    #doc.add_transaction(Transaction('Paypal', 111, datetime.now(), 1))
    #doc.add_transaction(Transaction('Stripe', 222, date.today(), 2))
    # Optional
    doc.set_bottom_tip("Email: ezreadcorp@gmail.com<br />No dudes en contactarnos para cualquier consulta.")
    doc.finish()

@app.route("/")
def main():
    return "<p>orden_crear</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True,port=5010)