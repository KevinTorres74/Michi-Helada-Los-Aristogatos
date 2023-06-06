from flask import session
from alchemyClasses.__init__ import db
from alchemyClasses.producto import Producto


def obten_producto(id_producto_arg):
    ans = Producto.query.filter(Producto.id_producto == id_producto_arg).first()
    return ans

def agregar_producto(producto):
    db.session.add(producto)
    db.session.commit()
