from alchemyClasses.producto import Producto


def obten_producto(id_producto_arg):
    ans = Producto.query.filter(Producto.id_producto == id_producto_arg).first()
    return ans
