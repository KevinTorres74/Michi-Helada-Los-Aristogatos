import functools
import sqlalchemy.exc
import datetime
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from alchemyClasses.vendedor import Vendedor
from alchemyClasses.__init__ import db

agregarVendedorBlueprint = Blueprint('agregarVendedor', __name__, url_prefix='/agregarVendedor')

@agregarVendedorBlueprint.route('/', methods=['GET', 'POST'])
def agregarVendedor():
    try:
        if request.method == 'POST':
            nombre = request.form['nombre']
            correo = request.form['correo']
            numero = request.form['phone']
            fnacimiento = request.form['fna']
            contrasena = request.form['password']

            # Validaciones de campos
            if any(char.isdigit() for char in nombre):
                return render_template('agregarVendedor.html', error='El nombre no puede contener números')

            if any(char.isalpha() for char in numero):
                return render_template('agregarVendedor.html', error='El teléfono no puede contener letras')

            selected_date = datetime.datetime.strptime(fnacimiento, '%Y-%m-%d').date()
            min_date = datetime.datetime.now().date() - datetime.timedelta(days=15 * 365)
            if selected_date >= datetime.datetime.now().date():
                return render_template('agregarVendedor.html', error='La fecha de nacimiento no puede ser posterior a la fecha actual')
            if selected_date >= min_date:
                return render_template('agregarVendedor.html', error='Debes tener al menos 15 años de edad')

            at_symbol_count = correo.count('@')
            if at_symbol_count != 1:
                return render_template('agregarVendedor.html', error='El correo debe contener el símbolo @ una vez')

            # Agregar a la base de datos de vendedor
            vendedor = Vendedor(nombre=nombre, correo=correo, telefono=numero, fna=fnacimiento, contraseña=contrasena)
            db.session.add(vendedor)
            db.session.commit()

            # obtener vendedor
            ans = Vendedor.query.filter(Vendedor.correo == correo).first()

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
        return render_template('agregarVendedor.html')


@agregarVendedorBlueprint.route('/success', methods=['GET'])
def success():
    if session.get('vendedor_id') is not None:
        return render_template("success.html")
    flash("ERROR: Cookie de sesion vacia")
    return redirect(url_for('agregarVendedor.agregarVendedor'))

@agregarVendedorBlueprint.route("/failure", methods=["GET"])
def failure():
    return render_template("failure.html")
