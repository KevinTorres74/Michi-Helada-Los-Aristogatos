from alchemyClasses.cliente import Cliente
from flask import session
from alchemyClasses.__init__ import db


#def agregar_cliente(id, nombre, correo, telefono, fna, contrasena):
    #nuevo_cliente = Cliente(id_cliente=id, nombre=nombre, correo=correo, telefono=telefono, fna=fna, contraseña=contrasena)
def agregar_cliente(cliente):
    db.session.add(cliente)
    db.session.commit()

def obten_cliente(id):
    ans = Cliente.query.filter(Cliente.id_cliente == id).first()
    return ans
