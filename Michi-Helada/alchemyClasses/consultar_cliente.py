import pymysql

"""
Consultar cliente --> Administrador
"""

# Conexion a la base de datos
#conexion1 = pymysql.connect(user='root', password='guadalupe',
#                           host='localhost', database='bdd-ingsoft',
#                           cursorclass=pymysql.cursors.DictCursor)

conexion1 = pymysql.connect(host='localhost', user='root', password='Josue318#',
                           database='ing_soft2',
                           cursorclass=pymysql.cursors.DictCursor)

with conexion1:
    with conexion1.cursor() as cursor:
        query1 = "SELECT * FROM cliente"
        cursor.execute(query1)
        respuesta1 = cursor.fetchall()
        total1 = cursor.rowcount


