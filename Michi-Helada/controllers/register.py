import functools
import sqlalchemy.exc
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from alchemyClasses.cliente import Cliente
from models.model_cliente import agregar_cliente
from models.model_cliente import obten_cliente

# maneja la logica de registrarse al sistema

registerBlueprint = Blueprint('register', __name__, url_prefix='/register')
# El nombre del blueprint para todos los demas en la aplcacion.
# #La ruta a la cual va a hacer handle o responder la peticion
#La ruta a la cual va a hacer handle o responder la peticion

@registerBlueprint.route('/', methods=['GET','POST'])
def register():
    try:
        # Recibe los datos
        if request.method == 'POST':
            id = request.form['id_cliente']
            nombre = request.form['nombre']
            correo = request.form['correo']
            numero = request.form['telefono']
            fnacimiento = request.form['fna']
            contrasena = request.form['contraseña']

            # Agregar a la base de datos al cliente
            cliente = Cliente(id_cliente=id, nombre=nombre, correo=correo, telefono=numero, fna=fnacimiento, contraseña=contrasena)
            agregar_cliente(cliente)

            if obten_cliente(id) != None:
                session.clear()
                session['cliente_id'] = cliente.id_cliente
                session['cliente_nombre'] = cliente.nombre
                g.user = cliente.nombre
            # Redirigir a una página de éxito o mostrar un mensaje de éxito
            return redirect(url_for("register.success"))

        else:
                return render_template('register.html')

    except sqlalchemy.exc.DataError as e:
        return  render_template('register.html')


@registerBlueprint.route('/success', methods=['GET'])
def success():
    if session.get('cliente_id') != None:
        return render_template("success.html")
    flash("ERROR: Cookie de sesion vacia")
    return redirect(url_for('register.register'))

@registerBlueprint.route("/failure", methods=["GET"])
def failure():
    return render_template("failure.html")
