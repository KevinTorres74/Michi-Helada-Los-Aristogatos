import pymysql
from flask import Flask, redirect, url_for
from alchemyClasses.cliente import db
from controllers.register import registerBlueprint
from controllers.loginAdmin import loginAdminBlueprint
from alchemyClasses.cliente import Cliente
from datetime import datetime
from models.model_cliente import agregar_cliente


try:
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='Josue318#',
        database='ing_soft',
        port=3306
    )
    print("Conexión exitosa a la base de datos")
    conn.close()
except pymysql.Error as e:
    print("Error al conectar a la base de datos:", e)


app = Flask(__name__, instance_relative_config=True)
app.register_blueprint(registerBlueprint)
app.register_blueprint(loginAdminBlueprint)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:Josue318#@localhost:3306/ing_soft"
app.config.from_mapping(
    SECRET_KEY = 'dev'
)
db.init_app(app)


@app.route('/', methods=['GET','POST'])
def hello_world():
    #nuevo_cliente = Cliente(id_cliente='None', nombre='Morales', correo='josuemt02@ciencias', telefono=55355416,
     #                       fna=datetime(2002, 8, 19), contraseña='contr')
    #db.session.add(nuevo_cliente)
    #db.session.commit()
    #agregar_cliente('None2', 'Josue Morales', 'josue@gmail.com', 35541645, datetime(2002, 8, 19), 'pruebas')
    return redirect(url_for('register.register'))

if __name__ == '__main__':
    db.create_all()
    app.run()
