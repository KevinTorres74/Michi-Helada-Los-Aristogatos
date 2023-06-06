import functools
import sqlalchemy.exc
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from alchemyClasses.cliente import Cliente
from alchemyClasses.__init__ import db

buscarClienteBlueprint = Blueprint('buscarCliente', __name__, url_prefix='/buscarCliente')

@buscarClienteBlueprint.route('/', methods=['GET', 'POST'])
def buscarCliente():
    if request.method == 'POST':
        correo = request.form.get('correo')

        # Validación de correo electrónico
        at_symbol_count = correo.count('@')
        if at_symbol_count != 1:
            flash('El correo debe contener el símbolo @ una vez', 'error')
            return redirect(url_for('buscarCliente.buscarCliente'))

        cliente = Cliente.query.filter_by(correo=correo).first()

        if cliente:
            return render_template('verCliente.html', cliente=cliente)
        else:
            flash('Correo no encontrado o incorrecto, intente nuevamente', 'error')

        return redirect(url_for('buscarCliente.buscarCliente'))

    return render_template('buscarCliente.html')
