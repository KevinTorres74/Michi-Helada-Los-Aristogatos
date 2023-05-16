import functools

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from alchemyClassses.cliente import Cliente
from mofels.model_cliente import agregar_cliente

# maneja la logica de registrarse al sistema

registerBlueprint = Blueprint('register',__name__,url_prefix='/register')
# El nombre del blueprint para todos los demas en la aplcacion.
# #La ruta a la cual va a hacer handle o responder la peticion
#La ruta a la cual va a hacer handle o responder la peticion

@registerBlueprint.route('/', methods=["GET", "POST"])
def register():
    # Recibe los datos
    if request.method == "POST":
        nombre = request.form["nombre"]
        correo = request.form["email"]
        numero = request.form["numero"]
        fnacimiento = request.form["nacimiento"]
        contraseña = request.form["password"]

        # Agregar a la base de datos al cliente
        agregar_cliente(nombre, correo, numero, fnacimiento,contraseña)

        # Redirigir a una página de éxito o mostrar un mensaje de éxito
        flash("Registro exitoso")
        return redirect(url_for('register.success'))

    return render_template('register.html')


@registerBlueprint.route('/success', methods=["GET"])
def success():
    if session.get('id_cliente') != None:
        return render_template("success.html")
    flash("ERROR: Cookie de sesion vacia")
    return redirect(url_for('login.login'))

@registerBlueprint.route("/failure", methods=["GET"])
def failure():
    return render_template("failure.html")
