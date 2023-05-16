from alchemyClasses.cliente import Cliente
from flask import session


def agregar_cliente(nombre, correo, telefono, fna, contrasena):
    nuevo_cliente = Cliente(nombre=nombre, correo=correo, telefono=telefono, fna=fna, contrasena=contrasena)
    session.add(nuevo_cliente)
    session.commit()
