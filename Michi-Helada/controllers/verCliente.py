import functools
import sqlalchemy.exc
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from alchemyClasses.cliente import Cliente
from alchemyClasses.__init__ import db

verClienteBlueprint = Blueprint('verCliente', __name__, url_prefix='/verCliente')

@verClienteBlueprint.route('/verCliente/<int:id_clienter>', methods=['GET'])
def verCliente(id_cliente):
    cliente = Cliente.query.get(id_cliente)

    if cliente:
        return render_template('verCliente.html', cliente=cliente)
    else:
        flash('No se encontró el cliente', 'error')
        return redirect(url_for('buscarCliente.buscarCliente'))
