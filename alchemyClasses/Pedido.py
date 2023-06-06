from alchemyClasses.__init__ import db


class Producto(db.Model):
    id_cliente = db.Column('id_cliente', db.String(200), primary_key=True)
    nombre = db.Column('nombre', db.String(45))
    precio = db.Column('precio', db.String(200))
    descripcion = db.Column('descripcion', db.integer)
    imagen = db.Column('imagen')
    disponibilidad = db.Column('disponibilidad', db.String(45))


def __init__(self, id_cliente, nombre, precio, descripcion, imagen, disponibilidad):
    self.id_cliente = id_cliente
    self.nombre = nombre
    self.precio = precio
    self.descripcion = descripcion
    self.imagen = imagen
    self.disponibildad = disponibilidad


def db():
    return None
