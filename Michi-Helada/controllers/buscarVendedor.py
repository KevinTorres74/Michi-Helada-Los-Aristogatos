import functools
import sqlalchemy.exc
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from alchemyClasses.vendedor import Vendedor
from alchemyClasses.__init__ import db

buscarVendedorBlueprint = Blueprint('buscarVendedor', __name__, url_prefix='/buscarVendedor')

@buscarVendedorBlueprint.route('/', methods=['GET', 'POST'])
def buscarVendedor():
    if request.method == 'POST':
        correo = request.form.get('correo')

        # Validación de correo electrónico
        at_symbol_count = correo.count('@')
        if at_symbol_count != 1:
            flash('El correo debe contener el símbolo @ una vez', 'error')
            return redirect(url_for('buscarVendedor.buscarVendedor'))

        vendedor = Vendedor.query.filter_by(correo=correo).first()

        if vendedor:
            return render_template('verVendedor.html', vendedor=vendedor)
        else:
            flash('Correo no encontrado o incorrecto, intente nuevamente', 'error')

        return redirect(url_for('buscarVendedor.buscarVendedor'))

    return render_template('buscarVendedor.html')
