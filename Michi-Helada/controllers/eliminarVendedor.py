import functools
import sqlalchemy.exc
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from alchemyClasses.vendedor import Vendedor
from alchemyClasses.__init__ import db

eliminarVendedorBlueprint = Blueprint('eliminarVendedor', __name__, url_prefix='/eliminarVendedor')

@eliminarVendedorBlueprint.route('/', methods=['GET', 'POST'])
def eliminarVendedor():
    if request.method == 'POST':
        id_vendedor = request.form['id_vendedor']

        vendedor = Vendedor.query.get(id_vendedor)
        if vendedor:
            db.session.delete(vendedor)
            db.session.commit()
            return redirect(url_for('eliminarVendedor.eliminarVendedor'))

    vendedores = Vendedor.query.all()
    return render_template('eliminarVendedor.html', vendedores=vendedores)
