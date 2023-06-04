from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, Flask
import pymysql
from flask_sqlalchemy import SQLAlchemy
from alchemyClasses.__init__ import db
from controllers.eliminarVendedor import eliminarVendedorBlueprint
from controllers.agregarVendedor import agregarVendedorBlueprint
from controllers.buscarVendedor import buscarVendedorBlueprint
from controllers.verVendedor import verVendedorBlueprint

app = Flask(__name__)

try:
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='Starmoon66680',
        database='ing_soft',
        port=3306
    )
    print("Conexión exitosa a la base de datos")
    conn.close()
except pymysql.Error as e:
    print("Error al conectar a la base de datos: ", e)


app = Flask(__name__, instance_relative_config=True)
app.register_blueprint(agregarVendedorBlueprint)
app.register_blueprint(eliminarVendedorBlueprint)
app.register_blueprint(buscarVendedorBlueprint)
app.register_blueprint(verVendedorBlueprint)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:Starmoon66680@localhost:3306/ing_soft"
app.config.from_mapping(
    SECRET_KEY = 'dev'
)
db.init_app(app)


@app.route('/', methods=['GET','POST'])
def hello_world():
    return redirect(url_for('agregarVendedor.agregarVendedor'))

if __name__ == '__main__':
    app.run(port = 3000, debug = True)
