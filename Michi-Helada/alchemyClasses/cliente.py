from alchemyClasses.__init__ import db
from sqlalchemy import text

class Cliente(db.Model):
    __tablename__ = 'cliente'

    #id_cliente = db.Column('id_cliente', db.String(200), primary_key=True, server_default=text('UUID()'))
    #id_cliente = db.Column('id_cliente', db.String(200), primary_key=True)
    id_cliente = db.Column('id_cliente', db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column('nombre', db.String(45))
    correo = db.Column('correo', db.String(45))
    telefono = db.Column('telefono', db.Integer)
    fna = db.Column('fna', db.Date)
    contraseña = db.Column('contraseña', db.String(45))



    def __init__(self, nombre, correo, telefono, fna, contraseña):
        #self.id_cliente = id_cliente
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.fna = fna
        self.contraseña = contraseña