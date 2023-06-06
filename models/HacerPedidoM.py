class Pedido:
    def __init__(self, nombre, direccion, producto, cantidad):
        self.nombre = nombre
        self.direccion = direccion
        self.producto = producto
        self.cantidad = cantidad

    def guardar(self):
        # Aquí puedes implementar la lógica para guardar el pedido en una base de datos o hacer alguna acción adicional

        # Ejemplo de impresión de los datos del pedido
        print(
            f"Pedido guardado: Nombre={self.nombre}, Dirección={self.direccion}, Producto={self.producto}, Cantidad={self.cantidad}")
