from flask import Blueprint, render_template, request

pedido_blueprint = Blueprint('pedido', __name__)


@pedido_blueprint.route('/pedido', methods=['GET', 'POST'])
def pedido():
    if request.method == 'POST':
        # Obtener los datos enviados por el formulario
        nombre = request.form['nombre']
        direccion = request.form['direccion']
        producto = request.form['producto']
        cantidad = request.form['cantidad']

        # Aquí puedes realizar alguna lógica adicional con los datos del pedido

        # Devolver una respuesta o redireccionar a otra página
        return render_template('PedidoSucces.html', nombre=nombre, producto=producto, cantidad=cantidad)

    # Si el método es GET, mostrar el formulario vacío
    return render_template('HacerPedido.html')
