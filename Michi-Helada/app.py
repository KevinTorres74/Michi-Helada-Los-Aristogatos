import pymysql
from flask import Flask, redirect, url_for
from alchemyClasses.cliente import db
from controllers.register import registerBlueprint
from controllers.loginAdmin import loginAdminBlueprint
from controllers.agregarProducto import agregarProductoBlueprint
from controllers.verProductos import verProductoBlueprint
from controllers.actualizarProducto import actualizarProductoBlueprint
from alchemyClasses.cliente import Cliente
from datetime import datetime
from models.model_cliente import agregar_cliente
from werkzeug.utils import secure_filename
from alchemyClasses.producto import Producto
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
import os





try:
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='Josue318#',
        database='ing_soft',
        port=3306
    )
    print("Conexión exitosa a la base de datos")
    conn.close()
except pymysql.Error as e:
    print("Error al conectar a la base de datos:", e)

UPLOAD_FOLDER = '/imagenes'
app = Flask(__name__, instance_relative_config=True)
app.register_blueprint(registerBlueprint)
app.register_blueprint(loginAdminBlueprint)
app.register_blueprint(agregarProductoBlueprint)
app.register_blueprint(verProductoBlueprint)
app.register_blueprint(actualizarProductoBlueprint)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:Josue318#@localhost:3306/ing_soft2"
UPLOAD_FOLDER = '/home/josuemt/PycharmProjects/Michi-Helada-Los-Aristogatos/Michi-Helada/imagenes'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'imagenes')
app.config.from_mapping(
    SECRET_KEY = 'dev'
)
db.init_app(app)


@app.route('/', methods=['GET','POST'])
def hello_world():
    return redirect(url_for('register.register'))


if __name__ == '__main__':
    db.create_all()
    app.run()
