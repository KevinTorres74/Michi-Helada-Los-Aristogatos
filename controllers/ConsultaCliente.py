from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for, app
from flask import request
from alchemyClasses.Cliente import Cliente
from models.ModelsCliente import obten_cliente
from alchemyClasses.Cliente import db

# Crear el Blueprint para la consulta de clientes
consulta_cliente_Blueprint = Blueprint('consulta_cliente', __name__, url_prefix='/consulta_cliente')


# Ruta para la página de consulta de clientes
@consulta_cliente_Blueprint.route('/consulta_cliente', methods=['GET'])
def consulta_cliente():
    return render_template('Consultacliente.html')


# Ruta para procesar la consulta de clientes
@consulta_cliente_Blueprint.route('/consulta_cliente', methods=['POST'])
def procesar_consulta_cliente():
    # Obtener los datos enviados desde el formulario
    id_cliente = request.form.get('id_cliente')

    # Aquí puedes implementar la lógica para buscar el cliente en la base de datos o hacer cualquier otra operación

    # Simplemente retornamos los datos del cliente como ejemplo
    cliente = {
        'id_cliente': id_cliente,
        'nombre': 'John Doe',
        'email': 'johndoe@example.com',
        'telefono': '1234567890'
    }

    return render_template('Consultaclientesucces.html', cliente=cliente)
