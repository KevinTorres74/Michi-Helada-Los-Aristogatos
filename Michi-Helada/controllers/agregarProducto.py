import functools
import sqlalchemy
from sqlalchemy import exc
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.utils import secure_filename
from alchemyClasses.producto import Producto
from models.model_producto import obten_producto
from models.model_producto import agregar_producto
from alchemyClasses.__init__ import db


agregarProductoBlueprint = Blueprint('agregarProducto', __name__, url_prefix='/agregarProducto')

def convertir_a_binario(imagen):
    blob = imagen.stream.read()
    return blob
@agregarProductoBlueprint.route('/', methods=['GET','POST'])
def agregarProducto():
    try:

        # Recibe los datos
        if request.method == 'POST':
            id_adminstrador = session['admin_id']
            nombre = request.form['nombre']
            precio = request.form['precio']
            descripcion = request.form['descripcion']
            #imagen = request.files['imagen']
            imagen = request.form['imagen']
            disponibilidad = bool(request.form.get('disponibilidad'))

            #Se crea el producto
            producto = Producto(id_administrador=id_adminstrador, nombre=nombre, precio=precio, descripcion=descripcion, imagen=imagen, disponibilidad=disponibilidad)
            db.session.add(producto)
            db.session.commit()


            if obten_producto(producto.id_producto) != None:

                flash("Se agrego el producto a la base de datos")
                return redirect(url_for("loginAdmin.success"))
            else:
                return  render_template('agregarProducto.html')
        else:  # Estamos haciendo un wget localhost:5000/login/
            return render_template('agregarProducto.html')

    except sqlalchemy.exc.DataError as e:
        return  render_template('agregarProducto.html')

@agregarProductoBlueprint.route('/success', methods=['GET'])
def success():
    if session.get('admin_id') != None:
        return render_template("success.html")
    flash("ERROR: Cookie de sesion vacia")
    return redirect(url_for('agregarProducto.agregarProducto'))

@agregarProductoBlueprint.route("/failure", methods=["GET"])
def failure():
    return render_template("failure.html")