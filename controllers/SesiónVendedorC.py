import functools
import sqlalchemy.exc
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from alchemyClasses.SesiónVendedor import Vendedor

loginVendedorBlueprint = Blueprint('loginVendedor', __name__, url_prefix='/loginVendedor')


@loginVendedorBlueprint.route('/', methods=['GET', 'POST'])
def loginVendedor():
    if request.method == 'POST':

        nombre = request.form['nombre']
        correo = request.form['correo']
        contrasena = request.form['contraseña']

        vendedor = Vendedor.query.filter_by(nombre=nombre, correo=correo, contraseña=contrasena).first()

        if vendedor != None:

            session.clear()
            session['vendedor_id'] = vendedor.id_vendedor
            session['vendedor_nombre'] = vendedor.nombre
            return redirect(url_for("loginVendedor.success"))
        else:
            return render_template('SesiónVendedor.html')
    else:
        return render_template('SesiónVendedor.html')


@loginVendedorBlueprint.route('/success', methods=['GET'])
def success():
    if session.get('admin_id') != None:
        return render_template("SVsucces.html")
    flash("ERROR: Cookie de sesion vacia")
    return redirect(url_for('loginVendedor.loginVendedor'))


@loginVendedorBlueprint.route("/failure", methods=["GET"])
def failure():
    return render_template("SVfailure.html")
