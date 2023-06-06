import functools
import sqlalchemy.exc
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from alchemyClasses.producto import Producto
from alchemyClasses.__init__ import db

eliminarProductoBlueprint = Blueprint('eliminarProducto', __name__, url_prefix='/eliminarProducto')

@eliminarProductoBlueprint.route('/', methods=['GET', 'POST'])
def eliminarProducto():
    if request.method == 'POST':
        id_producto = request.form['id_producto']

        producto = Producto.query.get(id_producto)
        if producto:
            db.session.delete(producto)
            db.session.commit()
            return redirect(url_for('eliminarProducto.eliminarProducto'))

    productos = Producto.query.all()
    return render_template('eliminarProducto.html', productos=productos)
