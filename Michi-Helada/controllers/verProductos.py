import functools
import sqlalchemy.exc
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for,Flask
from werkzeug.utils import secure_filename
from alchemyClasses.producto import Producto


#from models.model_cliente import agregar_cliente
verProductoBlueprint = Blueprint('verProducto', __name__, url_prefix='/verProducto')

@verProductoBlueprint.route('/', methods=['GET','POST'])
def verProducto():

    productos = Producto.query.all()
    columnas_excluidas = ['id_producto', 'id_administrador']
    columnas_mostradas = [columna.name for columna in Producto.__table__.columns if columna.name not in columnas_excluidas]
    return render_template('tabla_productos.html', getattr=getattr, productos=productos, columnas_mostradas=columnas_mostradas)