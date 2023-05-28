from alchemyClasses.cliente import Cliente


def obten_cliente(id_cliente_arg):
    ans = Cliente.query.filter(Cliente.id_cliente == id_cliente_arg).first()
    return ans