from alchemyClasses.__init__ import db


class Administrador(db.Model):
    __tablename__ = 'administrador'

    id_administrador = db.Column('id_administrador', db.String(200), primary_key=True)
    nombre = db.Column('nombre', db.String(45))
    correo = db.Column('correo', db.String(45))
    telefono = db.Column('telefono', db.Integer)
    fna = db.Column('fna', db.Date)
    contraseña = db.Column('contraseña', db.String(45))

    def __init__(self, id_administrador, nombre, correo, telefono, fna, contraseña):
        self.id_administrador = id_administrador
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.fna = fna
        self.contraseña = contraseña
