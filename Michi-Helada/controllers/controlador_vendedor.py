from alchemyClasses.upd_vendedor import *


# Metodo para obtener una lista de todos los vendedores.
def obtener_vendedores():
    conexion = obtener_conexion()
    vendedores = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id_vendedor, nombre, correo, telefono, fna, contraseña FROM vendedor")
        vendedores = cursor.fetchall()
    conexion.close()
    return vendedores


# Metodo para seleccionar a un vendedor en especifico.
def obtener_vendedor_por_id(id):
    conexion = obtener_conexion()
    vendedor = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id_vendedor, nombre, correo, telefono, fna, contraseña FROM vendedor WHERE id_vendedor = %s", (id,))
        vendedor = cursor.fetchone()
    conexion.close()
    return vendedor


# Metodo que actualiza los valores en la BD.
def actualizar_vendedor(nombre, correo, telefono, fna, contraseña, id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute(
            "UPDATE vendedor SET nombre = %s, correo = %s, telefono = %s, fna = %s, contraseña = %s WHERE id_vendedor = %s",
            (nombre, correo, telefono, fna, contraseña, id))
    conexion.commit()
    conexion.close()
