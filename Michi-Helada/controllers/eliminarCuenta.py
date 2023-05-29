from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from alchemyClasses.cliente import Cliente
from models.model_cliente import obten_id_cliente
from alchemyClasses.cliente import db

eliminarCuentaBlueprint = Blueprint('eliminarCuenta', __name__, url_prefix='/eliminarCuenta')


@eliminarCuentaBlueprint.route('/', methods=["GET", "POST"])
def eliminarCuenta():
    if request.method == "POST":
        correo = request.form["correo"]
        contraseña = request.form["contraseña"]
        id_cliente = obten_id_cliente(correo, contraseña)
        if id_cliente != None:
            Cliente.query.filter_by(id_cliente=id_cliente).delete()
            db.session.commit()
            print("Se eliminó la cuenta de la base de datos.")
            return redirect(url_for('eliminarCuenta.success'))
        else:
            print("El correo o contraseña ingresados no están asociados a una cuenta.")
            return redirect(url_for('eliminarCuenta.failure'))
    else:
        return render_template('eliminarCuenta.html')


@eliminarCuentaBlueprint.route('/success', methods=["GET"])
def success():
    return render_template("eliminarCuentaSuccess.html")


@eliminarCuentaBlueprint.route('/failure', methods=["GET"])
def failure():
    return render_template("eliminarCuentaFailure.html")