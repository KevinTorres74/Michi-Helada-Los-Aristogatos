from alchemyClasses


def obten_cliente(id_cliente_arg):
    ans = Cliente.query.filter(Cliente.id_cliente == id_cliente_arg).first()
    return ans


def obten_id_cliente(correo_arg, contraseña_arg):
    cliente = Cliente.query.filter_by(correo=correo_arg, contraseña=contraseña_arg).first()
    if cliente is not None:
        return cliente.id_cliente
    else:
        return None
