from alchemyClasses.__init__ import db
from sqlalchemy import ForeignKey

class Producto(db.Model):
    __tablename__ = 'producto'

    id_producto = db.Column('id_producto', db.Integer, primary_key=True, autoincrement=True)
    id_administrador = db.Column('id_administrador', db.Integer, ForeignKey('administrador.id_administrador'))
    nombre = db.Column('nombre', db.String(45))
    precio = db.Column('precio', db.Float)
    descripcion = db.Column('descripcion', db.String(200))
    imagen = db.Column('imagen', db.String(200))
    disponibilidad = db.Column('disponibilidad', db.Boolean)

    def __init__(self, id_administrador, nombre, precio, descripcion, imagen, disponibilidad):
        self.id_administrador = id_administrador
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.imagen = imagen
        self.disponibilidad = disponibilidad