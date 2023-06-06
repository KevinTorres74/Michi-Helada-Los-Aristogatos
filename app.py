from flask import Flask
import pymysql

from flask import Flask, redirect, url_for

from alchemyClasses.Cliente import db
from controllers.ConsultaCliente import consulta_cliente_blueprint
from controllers.VerProductoC import verProductoBlueprint
from controllers.HacerPedido import pedido
from controllers.SesiónVendedorC import login
from alchemyClasses.Cliente import Cliente
from alchemyClasses.VerProducto import Producto
from alchemyClasses.Pedido import Producto
from alchemyClasses.SesiónVendedor import vendedor
from datetime import datetime
from models.VerProductoM import Producto
from models.ModelsCliente import Cliente
from models.HacerPedidoM import Pedido
from models.SesiónVendedorM import vendedor
from werkzeug.utils import secure_filename
from flask import Flask

app = Flask(__name__)
app.register_blueprint(pedido_blueprint)

if __name__ == '__main__':
    app.run(debug=True)

app = Flask(__name__)

app.register_blueprint(consultaclienteBlueprint)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root: Jimmypage1970@localhost:3306/bdd-ingsoft'
app.config.from_mapping(
    SECRET_KEY='dev'
)
db.init_app(app)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(route=5000, debug=True)
