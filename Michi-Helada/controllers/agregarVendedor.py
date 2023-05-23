import functools
import sqlalchemy.exc
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from alchemyClasses.vendedor import Vendedor
from alchemyClasses.__init__ import db

# maneja la logica de registrar un vendedor

agregarVendedorBlueprint = Blueprint('agregarVendedor', __name__, url_prefix='/agregarVendedor')


@agregarVendedorBlueprint.route('/', methods=['GET','POST'])
def agregarVendedor():
    try:
        # Recibe los datos
        if request.method == 'POST':
            id = request.form['id']
            nombre = request.form['nombre']
            correo = request.form['correo']
            numero = request.form['phone']
            fnacimiento = request.form['fna']
            contrasena = request.form['password']

            # Agregar a la base de datos de vendedor
            vendedor = Vendedor(id_vendedor=id, nombre=nombre, correo=correo, telefono=numero, fna=fnacimiento, contraseña=contrasena)
            db.session.add(vendedor)
            db.session.commit()


            #obtener vendedor
            ans = Vendedor.query.filter(Vendedor.id_vendedor == id).first()

            if ans != None:
                session.clear()
                session['vendedor_id'] = vendedor.id_vendedor
                session['vendedor_nombre'] = vendedor.nombre
                g.user = vendedor.nombre
            # Redirigir a una página de éxito o mostrar un mensaje de éxito
            return redirect(url_for("agregarVendedor.success"))

        else:
                return render_template('agregarVendedor.html')

    except sqlalchemy.exc.DataError as e:
        return  render_template('agregarVendedor.html')


@agregarVendedorBlueprint.route('/success', methods=['GET'])
def success():
    if session.get('vendedor_id') != None:
        return render_template("success.html")
    flash("ERROR: Cookie de sesion vacia")
    return redirect(url_for('agregarVendedor.agregarVendedor'))

@agregarVendedorBlueprint.route("/failure", methods=["GET"])
def failure():
    return render_template("failure.html")