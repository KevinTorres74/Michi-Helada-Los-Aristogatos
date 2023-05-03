from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()
#Conexion a la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:1234@localhost:3306/Prueba"
app.config.from_mapping(
    SECRET_KEY='dev'
)
db.init_app(app)

#Para probar se hace un print
print("conexion exitosa")

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
