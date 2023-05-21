
"""
Consultar reporte de venta
"""
from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Conéctate a la base de datos
conexion = mysql.connector.connect(user='usuario', password='contraseña',
                              host='host', database='basedatos')

# Crea un cursor para realizar consultas
cursor = conexion.cursor()

# Ejecuta una consulta SQL para obtener el reporte de venta
query = "SELECT fecha, producto.py, cantidad, precio FROM ventas"
cursor.execute(query)

# Obtiene los resultados de la consulta
resultados = cursor.fetchall()

# Renderiza el template con los resultados
@app.route('/')
def mostrar_reporte_venta():
    return render_template('reporte.html', resultados=resultados)

# Cierra la conexión a la base de datos
conexion.close()


"""
Consultar Cliente
"""
from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Conéctate a la base de datos
conexion = mysql.connector.connect(user='usuario', password='contraseña',
                              host='host', database='basedatos')

# Crea un cursor para realizar consultas
cursor = conexion.cursor()

# Ejecuta una consulta SQL para obtener la información del cliente
query = "SELECT nombre, correo, telefono FROM clientes WHERE id = %s"
cliente_id = 1  # ID del cliente que deseas consultar
cursor.execute(query, (cliente_id,))

# Obtiene los resultados de la consulta
resultados = cursor.fetchall()

# Renderiza el template con los resultados
@app.route('/')
def mostrar_informacion_cliente():
    return render_template('cliente.html', resultados=resultados)

# Cierra la conexión a la base de datos
conexion.close()


"""
Actualizar la contraseña de un vendedor
"""
from flask import render_template, redirect, url_for, flash
from flask_login import current_user, login_required
from .forms import UpdatePasswordForm
from .models import User
from . import db

@app.route('/update_password', methods=['GET', 'POST'])
@login_required
def update_password():
    form = UpdatePasswordForm()
    if form.validate_on_submit():
        user = User.query.filter_by(id=current_user.id).first()
        if user is not None and user.verify_password(form.current_password.data):
            user.password = form.new_password.data
            db.session.commit()
            flash('Password updated successfully.')
            return redirect(url_for('index'))
        flash('Invalid current password.')
    return render_template('update_password.html', form=form)

