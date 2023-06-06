import functools
import sqlalchemy.exc
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from alchemyClasses.vendedor import Vendedor
from alchemyClasses.__init__ import db

verVendedorBlueprint = Blueprint('verVendedor', __name__, url_prefix='/verVendedor')

@verVendedorBlueprint.route('/verVendedor/<int:id_vendedor>', methods=['GET'])
def verVendedor(id_vendedor):
    # Buscar el vendedor por su correo
    vendedor = Vendedor.query.get(id_vendedor)

    if vendedor:
        return render_template('verVendedor.html', vendedor=vendedor)
    else:
        flash('No se encontró el vendedor', 'error')
        return redirect(url_for('buscarVendedor.buscarVendedor'))
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from alchemyClasses.vendedor import Vendedor

verVendedorBlueprint = Blueprint('verVendedor', __name__, url_prefix='/verVendedor')


@verVendedorBlueprint.route('/', methods=["GET", "POST"])
def verVendedor():
    vendedores = Vendedor.query.all()
    columnas = [columna.name for columna in Vendedor.__table__.columns if
                columna.name != "contraseña"]
    return render_template('verVendedor.html', getattr=getattr, vendedores=vendedores,
                           columnas=columnas)
