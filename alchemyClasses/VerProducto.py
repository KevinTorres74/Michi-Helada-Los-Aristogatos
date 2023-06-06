from alchemyClasses.__init__ import db
from sqlalchemy import ForeignKey

class Producto(db.Model):
    __tablename__ = 'Producto'

    #id_producto = db.Column('id_producto', db.String(200), primary_key=True)
    id_producto = db.Column('id_producto', db.Integer, primary_key=True, autoincrement=True)
    id_cliente = db.Column('id_cliente', db.Integer, ForeignKey('cliente.id_cliente'))
    nombre = db.Column('nombre', db.String(45))
    precio = db.Column('precio', db.Float)
    descripcion = db.Column('descripcion', db.String(200))
    imagen = db.Column('imagen', db.String(200))
    disponibilidad = db.Column('disponibilidad', db.Boolean)


    def __init__(self, id_cliente, nombre, precio, descripcion, imagen, disponibilidad):
        #self.id_producto = id_producto
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.imagen = imagen
        self.disponibilidad = disponibilidad