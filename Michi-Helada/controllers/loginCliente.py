import functools
import sqlalchemy.exc
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from alchemyClasses.cliente import Cliente
loginClienteBlueprint = Blueprint('loginCliente', __name__, url_prefix='/loginCliente')

@loginClienteBlueprint.route('/', methods=['GET','POST'])
def loginCliente():

        # Recibe los datos
        if request.method == 'POST':

            nombre = request.form['nombre']
            correo = request.form['correo']
            contrasena = request.form['contraseña']

            #verifica que este en la base de datos de cliente
            cliente = Cliente.query.filter_by(nombre=nombre, correo=correo, contraseña=contrasena).first()


            if cliente != None:

                session.clear()
                session['cliente_id'] = cliente.id_cliente
                session['cliente_nombre'] = cliente.nombre
                return redirect(url_for("loginCliente.success"))
            else:
                return  render_template('loginCliente.html')
        else:  # Estamos haciendo un wget localhost:5000/login/
            return render_template('loginCliente.html')

@loginClienteBlueprint.route('/success', methods=['GET'])
def success():
    if session.get('cliente_id') != None:
        return render_template("success.html")
    flash("ERROR: Cookie de sesion vacia")
    return redirect(url_for('loginCliente.loginCliente'))

@loginClienteBlueprint.route("/failure", methods=["GET"])
def failure():
    return render_template("failure.html")
