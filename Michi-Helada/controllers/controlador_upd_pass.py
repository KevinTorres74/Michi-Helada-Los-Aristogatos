from alchemyClasses.upd_vendedor import *


# Metodo para obtener una lista de todos los vendedores.
def obtener_pass():
    conexion = obtener_conexion()
    contrasenias = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id_vendedor, nombre, correo, contraseña FROM vendedor")
        contrasenias = cursor.fetchall()
    conexion.close()
    return contrasenias


# Metodo para seleccionar a un vendedor en especifico.
def obtener_pass_por_id(id):
    conexion = obtener_conexion()
    contrasenia = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id_vendedor, nombre, correo, contraseña FROM vendedor WHERE id_vendedor = %s", (id,))
        contrasenia = cursor.fetchone()
    conexion.close()
    return contrasenia


# Metodo que actualiza los valores en la BD.
def actualizar_pass(contraseña, id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute(
            "UPDATE vendedor SET contraseña = %s WHERE id_vendedor = %s",
            (contraseña, id))
    conexion.commit()
    conexion.close()
