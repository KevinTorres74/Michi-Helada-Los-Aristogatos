#from flask import Flask
#import mysql.connector
import pymysql

"""
Consultar reporte de venta-Administrador
"""

# Conexion a la base de datos
#conexion = pymysql.connect(user='root', password='guadalupe',
#                           host='localhost', database='bdd-ingsoft',
#                           cursorclass=pymysql.cursors.DictCursor)

conexion = pymysql.connect(host='localhost', user='root', password='Josue318#',
                           database='ing_soft2',
                           cursorclass=pymysql.cursors.DictCursor)

"""
# Crea un cursor para realizar consultas
cursor = conexion.cursor()

# Ejecuta una consulta SQL para obtener el reporte de venta
query = "SELECT * FROM reportedeventa"
cursor.execute(query)

# Obtiene los resultados de la consulta
resultados = cursor.fetchall()

# Cierra la conexión a la base de datos
conexion.close()
"""
with conexion:
    with conexion.cursor() as cursor:
        #query = "SELECT * FROM reportedeventa"
        query = "SELECT * FROM reporteDeVenta"
        cursor.execute(query)
        respuesta = cursor.fetchall()
        total = cursor.rowcount
        #print(respuesta)
        #conexion.close()