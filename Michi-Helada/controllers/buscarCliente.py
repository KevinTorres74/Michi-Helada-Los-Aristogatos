from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from alchemyClasses.cliente import Cliente
from models.model_cliente import obten_cliente
from alchemyClasses.cliente import db

buscarClienteBlueprint = Blueprint('buscarCliente', __name__, url_prefix='/buscarCliente')


@buscarClienteBlueprint.route('/', methods=["GET", "POST"])
def buscarCliente():
    if request.method == "POST":
        id_cliente = request.form["id_cliente"]
        cliente = obten_cliente(id_cliente)
        if cliente != None:
            print("Se encontró el cliente!.")
            return render_template('buscarClienteSuccess.html', getattr=getattr, cliente=cliente)
        else:
            print("No existe cliente con el id " + str(id_cliente) + ".")
            return redirect(url_for('buscarCliente.failure'))
    else:
        return render_template('buscarCliente.html')


@buscarClienteBlueprint.route('/failure', methods=["GET"])
def failure():
    return render_template("buscarClienteFailure.html")