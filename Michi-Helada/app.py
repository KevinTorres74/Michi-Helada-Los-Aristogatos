from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

try:
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='Starmoon66680',
        database='ing_soft',
        port=3306
    )
    print("Conexión exitosa a la base de datos")
    conn.close()
except pymysql.Error as e:
    print("Error al conectar a la base de datos: ", e)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
