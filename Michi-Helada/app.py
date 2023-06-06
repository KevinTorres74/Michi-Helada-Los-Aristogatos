from flask import Flask, render_template, redirect, url_for, request
from alchemyClasses.mostrar_reporte_venta import *
from alchemyClasses.consultar_cliente import *
from controllers import controlador_vendedor, controlador_upd_pass

import pymysql
from alchemyClasses.cliente import db
from controllers.register import registerBlueprint
from controllers.loginAdmin import loginAdminBlueprint
from controllers.agregarProducto import agregarProductoBlueprint
from controllers.verProductos import verProductoBlueprint
from controllers.actualizarProducto import actualizarProductoBlueprint
from controllers.eliminarVendedor import eliminarVendedorBlueprint
from controllers.agregarVendedor import agregarVendedorBlueprint
from controllers.buscarVendedor import buscarVendedorBlueprint
from controllers.verVendedor import verVendedorBlueprint
from controllers.eliminarProducto import eliminarProductoBlueprint
from controllers.buscarCliente import buscarClienteBlueprint
from controllers.eliminarCuenta import eliminarCuentaBlueprint
from controllers.verVendedor import verVendedorBlueprint
from alchemyClasses.producto import db
from alchemyClasses.cliente import Cliente
#from models.model_cliente import agregar_cliente
from werkzeug.utils import secure_filename
from alchemyClasses.producto import Producto
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
import os
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, Flask
import pymysql
from flask_sqlalchemy import SQLAlchemy
from alchemyClasses.__init__ import db


app = Flask(__name__)

# Consultar reporte de venta --> Administrador.
@app.route('/reporteVenta', methods=['GET', 'POST'])
def mostrar_reporte_venta():
    return render_template('viewReporte/reporte.html', respuesta=respuesta, total=total)


# Redireccionando cuando la página no existe
@app.errorhandler(404)
def not_found(error):
    return redirect(url_for('mostrar_reporte_venta'))


# Consultar Cliente --> Administrador.
@app.route('/clientes', methods=['GET', 'POST'])
def mostrar_consulta_cliente():
    return render_template('viewCliente/selCliente.html', respuesta1=respuesta1, total1=total1)


# Redireccionando cuando la página no existe
@app.errorhandler(404)
def not_found(error):
    return redirect(url_for('mostrar_consulta_cliente'))


# Actualizar Vendedor --> Administrador.

# Se define la ruta para ver a todos los vendedores.
@app.route("/")
@app.route("/vendedores")
def vendedores():
    vendedores = controlador_vendedor.obtener_vendedores()
    return render_template("viewVendedor/vendedores.html", vendedores=vendedores)


# Se define la ruta para modificar a un vendedor.
@app.route("/formulario_editar_vendedor/<int:id>")
def editar_vendedor(id):
    # Obtener el vendedor por ID
    vendedor = controlador_vendedor.obtener_vendedor_por_id(id)
    return render_template("viewVendedor/editar_vendedor.html", vendedor=vendedor)


# Se define la ruta para actualizar los datos de un vendedor.
@app.route("/actualizar_vendedor", methods=["POST"])
def actualizar_vendedor():
    id = request.form["id"]
    nombre = request.form["nombre"]
    correo = request.form["correo"]
    telefono = request.form["tel"]
    fna = request.form["fna"]
    contrasenia = request.form["pass"]
    controlador_vendedor.actualizar_vendedor(nombre, correo, telefono, fna, contrasenia, id)
    return redirect("/vendedores")


# Redireccionando cuando la página no existe
@app.errorhandler(404)
def not_found(error):
    return redirect(url_for('vendedores'))


# Actualizar Contraseña --> Vendedor.

# Se define la ruta para ver la configuracion.
# @app.route("/")
@app.route("/configPerfil")
def passws():
    contrasenias = controlador_upd_pass.obtener_pass()
    return render_template("viewUpdPass/configPerfil.html", contrasenias=contrasenias)

# Se define la ruta para modificar a un vendedor.
@app.route("/formulario_editar_contrasenia/<int:id>")
def editar_pass(id):
    # Obtener el contrasenia por ID
    contrasenia = controlador_upd_pass.obtener_pass_por_id(id)
    return render_template("viewUpdPass/editar_pass.html", contrasenia=contrasenia)

# Se define la ruta para actualizar los datos de un vendedor.
@app.route("/actualizar_contrasenia", methods=["POST"])
def actualizar_pass():
    id = request.form["id"]
    contrasenia = request.form["pass"]
    controlador_upd_pass.actualizar_pass(contrasenia, id)
    return redirect("/configPerfil")

# Redireccionando cuando la página no existe
@app.errorhandler(404)
def not_found(error):
    return redirect(url_for('passws'))

app = Flask(__name__, instance_relative_config=True)
app.register_blueprint(registerBlueprint)
app.register_blueprint(loginAdminBlueprint)
app.register_blueprint(agregarProductoBlueprint)
app.register_blueprint(verProductoBlueprint)
app.register_blueprint(actualizarProductoBlueprint)
app.register_blueprint(eliminarProductoBlueprint)
app.register_blueprint(buscarClienteBlueprint)
app.register_blueprint(eliminarCuentaBlueprint)
app.register_blueprint(verVendedorBlueprint)
app.register_blueprint(agregarVendedorBlueprint)
app.register_blueprint(eliminarVendedorBlueprint)
app.register_blueprint(buscarVendedorBlueprint)
#app.register_blueprint(verVendedorBlueprint)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:Josue318#@localhost:3306/ing_soft2"
app.config.from_mapping(
    SECRET_KEY = 'dev'
)
db.init_app(app)

@app.route('/', methods=['GET','POST'])
def hello_world():
    return redirect(url_for('register.register'))




@app.route('/', methods=['GET','POST'])
def agregarNuevoVendedor():
    return redirect(url_for('agregarVendedor.agregarVendedor'))

if __name__ == '__main__':
    db.create_all()
    app.run()
    #app.run(port = 3000, debug = True)
