from alchemyClasses.producto import Producto
from flask import session
from alchemyClasses.__init__ import db

def obten_producto(id):
    ans = Producto.query.filter(Producto.id_producto == id).first()
    return ans

def agregar_producto(producto):
    db.session.add(producto)
    db.session.commit()
