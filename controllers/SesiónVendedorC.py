from flask import Blueprint, render_template, request, redirect, url_for, session

# Crear el Blueprint para la autenticación y el manejo de sesión
auth_blueprint = Blueprint('auth', __name__)


# Ruta para el inicio de sesión del vendedor
@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Obtener los datos del formulario
        username = request.form['username']
        password = request.form['password']

        # Aquí puedes implementar la lógica de autenticación
        # Verificar si el vendedor existe en la base de datos y si la contraseña es correcta

        # Ejemplo de autenticación básica
        if username == 'vendedor' and password == 'vendedor123':
            # Establecer la sesión del vendedor
            session['username'] = username
            return redirect(url_for('main.dashboard'))
        else:
            # Si las credenciales son incorrectas, mostrar un mensaje de error
            error_message = 'Credenciales inválidas. Inténtalo de nuevo.'
            return render_template('SesiónVendedor.html', error_message=error_message)

    # Si el método es GET, mostrar el formulario de inicio de sesión
    return render_template('login.html')


# Ruta para cerrar sesión del vendedor
@auth_blueprint.route('/logout')
def logout():
    # Eliminar la sesión del vendedor
    session.pop('username', None)
    return redirect(url_for('auth.login'))
