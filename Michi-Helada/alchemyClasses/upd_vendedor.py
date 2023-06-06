import pymysql


def obtener_conexion():
#    return pymysql.connect(host='localhost',
#                           user='root',
#                           password='guadalupe',
#                           db='bdd-ingsoft')
    return pymysql.connect(
        host='localhost',
        user='root',
        password='Josue318#',
        database='ing_soft',
        port=3306
    )