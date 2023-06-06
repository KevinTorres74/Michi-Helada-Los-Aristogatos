import functools
import sqlalchemy.exc
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from alchemyClasses.administrador import Administrador
#from models.model_cliente import agregar_cliente
loginAdminBlueprint = Blueprint('loginAdmin', __name__, url_prefix='/loginAdmin')

@loginAdminBlueprint.route('/', methods=['GET','POST'])
def loginAdmin():

        # Recibe los datos
        if request.method == 'POST':

            nombre = request.form['nombre']
            correo = request.form['correo']
            contrasena = request.form['contraseña']

            #verifica que este en la base de datos de administrador
            administrador = Administrador.query.filter_by(nombre=nombre, correo=correo, contraseña=contrasena).first()


            if administrador != None:

                session.clear()
                session['admin_id'] = administrador.id_administrador
                session['admin_nombre'] = administrador.nombre
                return redirect(url_for("loginAdmin.success"))
            else:
                return  render_template('loginAdmin.html')
        else:  # Estamos haciendo un wget localhost:5000/login/
            return render_template('loginAdmin.html')

@loginAdminBlueprint.route('/success', methods=['GET'])
def success():
    if session.get('admin_id') != None:
        return render_template("success.html")
    flash("ERROR: Cookie de sesion vacia")
    return redirect(url_for('loginAdmin.loginAdmin'))

@loginAdminBlueprint.route("/failure", methods=["GET"])
def failure():
    return render_template("failure.html")