from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from flask import request
from alchemyClasses.Cliente import Cliente
from models.model_cliente import obten_cliente
from alchemyClasses.Cliente import db

consultaclienteBlueprint = Blueprint('consultacliente', __name__, url_prefix='/consultacliente')


@consultaclienteBlueprint.route('/', methods=["GET", "POST"])
def consultacliente():
    if request.method == "POST":
    # Recibe datos
    id_cliente = request.form["id_cliente"]
    cliente = obten_cliente(id_cliente)


if Cliente != None:
    print("Cliente consultado")
    return render_template(Consultaclientesucces.html
    ')
    else:
    print("Cliente no consultado" + str(id_cliente) + ".")

return redirect(url_for('Consultacliente.failure'))

else:
return render_template('Consultacliente.html')


# Si existen los datos: acepta
# Si no existen: rechaza
@consultaclienteBlueprint.route('/failure', methods=["GET"])
def failure():
    return render_template("consultacliente.html.html")
