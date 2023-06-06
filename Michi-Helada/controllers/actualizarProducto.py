import functools
import sqlalchemy.exc
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.utils import secure_filename
from alchemyClasses.producto import Producto
from models.model_producto import obten_producto
from models.model_producto import agregar_producto
from alchemyClasses.__init__ import db
from controllers import verProductos
from controllers.verProductos import verProductoBlueprint

actualizarProductoBlueprint = Blueprint('actualizarProducto', __name__, url_prefix='/actualizarProducto')

@actualizarProductoBlueprint.route('/', methods=['GET', 'POST'])
def actualizarProducto():
    try:
        if request.method == 'POST':
            nombre = request.form['nombre']
            precio = request.form['precio']
            descripcion = request.form['descripcion']
            imagen = request.form['imagen']
            disponibilidad = bool(request.form.get('disponibilidad'))

            id_producto = request.form['id_producto']

            # Realizar la actualización del producto según el id_producto
            producto = obten_producto(id_producto)

            if producto is not None:
                producto.nombre = nombre
                producto.precio = precio
                producto.descripcion = descripcion
                producto.imagen = imagen
                producto.disponibilidad = disponibilidad

                db.session.commit()

                #flash("El producto se ha actualizado")
                return redirect(url_for("verProducto.verProducto"))
            else:
                flash("No se encontró el producto.")
                return redirect(url_for("verProducto.verProducto"))
        else:
            id_producto = request.args.get('id_producto')

            # Obtener el producto según el id_producto y pasarlo al template
            producto = obten_producto(id_producto)

            if producto is not None:
                return render_template('actualizarProducto.html', producto=producto)
            else:
                flash("No se encontró el producto.")
                return redirect(url_for("verProducto.verProducto"))
    except Exception as e:
        flash("Error al actualizar el producto.")
        return redirect(url_for("verProducto.verProducto"))
