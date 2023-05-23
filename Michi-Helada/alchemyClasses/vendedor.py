from alchemyClasses.__init__ import db
from sqlalchemy import text

class Vendedor(db.Model):
    __tablename__ = 'vendedor'

    id_vendedor = db.Column('id_vendedor', db.String(200), primary_key=True)
    nombre = db.Column('nombre', db.String(45))
    correo = db.Column('correo', db.String(45))
    telefono = db.Column('telefono', db.Integer)
    fna = db.Column('fna', db.Date)
    contraseña = db.Column('contraseña', db.String(45))



    def __init__(self, id_vendedor, nombre, correo, telefono, fna, contraseña):
        self.id_vendedor = id_vendedor
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.fna = fna
        self.contraseña = contraseña