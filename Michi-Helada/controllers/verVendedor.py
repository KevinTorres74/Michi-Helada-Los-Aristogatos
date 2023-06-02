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