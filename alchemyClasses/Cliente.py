from alchemyClasses.__init__ import db


class Cliente(db.Model):
    id_cliente = db.Column('id_cliente', db.String(200), primary_key=True)
    nombre = db.Column('nombre', db.String(45))
    correo = db.Column('correo', db.String(200))
    telefono = db.Column('telefono', db.integer)
    fna = db.Column('fna', db.Date)
    contraseña = db.Column('contraseña', db.String(45))


def __init__(self, id_cliente, nombre, correo, telefono, fna, contraseña):
    self.id_cliente = id_cliente
    self.nombre = nombre
    self.correo = correo
    self.telefono = telefono
    self.fna = fna
    self.contraseña = contraseña


def db():
    return None
