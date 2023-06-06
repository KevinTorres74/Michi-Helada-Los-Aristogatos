from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from alchemyClasses.producto import Producto
from models.model_producto import obten_producto
from alchemyClasses.producto import db

eliminarProductoBlueprint = Blueprint('eliminarProducto', __name__, url_prefix='/eliminarProducto')


@eliminarProductoBlueprint.route('/', methods=["GET", "POST"])
def eliminarProducto():
    if request.method == "POST":
        id_producto = request.form["id_producto"]
        if obten_producto(id_producto) != None:
            Producto.query.filter_by(id_producto=id_producto).delete()
            db.session.commit()
            print("Se eliminó el producto de la base de datos.")
            return redirect(url_for('eliminarProducto.success'))
        else:
            print("No existe el producto.")
            return redirect(url_for('eliminarProducto.failure'))
    else:
        return render_template('eliminarProducto.html')


@eliminarProductoBlueprint.route('/success', methods=["GET"])
def success():
    return render_template("eliminarProductoSuccess.html")


@eliminarProductoBlueprint.route('/failure', methods=["GET"])
def failure():
    return render_template("eliminarProductoFailure.html")