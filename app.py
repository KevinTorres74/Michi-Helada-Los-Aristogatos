from flask import Flask
import pymysql

from flask import Flask, redirect, url_for
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from alchemyClasses.Cliente import db

from controllers.ConsultaCliente import consulta_cliente_Blueprint
from controllers.VerProductoC import verProductoBlueprint
from controllers.HacerPedido import pedido
from controllers.SesiónVendedorC import loginVendedorBlueprint
from alchemyClasses.Cliente import Cliente
from alchemyClasses.VerProducto import Producto
from alchemyClasses.Pedido import Producto

from datetime import datetime
from models.VerProductoM import Producto
from models.ModelsCliente import Cliente
from models.HacerPedidoM import Pedido
from models.SesiónVendedorM import Vendedor
from werkzeug.utils import secure_filename
from flask import Flask
import os


try:
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='Jimmypage1970',
        database='ing_soft1',
        port=3306
    )
    print("Conexión exitosa a la base de datos")
    conn.close()
except pymysql.Error as e:
    print("Error al conectar a la base de datos:", e)

app.register_blueprint(consulta_cliente_Blueprint)
app.register_blueprint(HacerPedidoBlueprint)
app.register_blueprint(SesiónVendedorBlueprint)
app.register_blueprint(VerProductoBlueprint)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root: Jimmypage1970@localhost:3306/ing_soft1'
app.config.from_mapping(
    SECRET_KEY='dev'
)
db.init_app(app)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(port=3306, debug=True)
