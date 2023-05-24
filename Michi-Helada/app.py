from flask import Flask
from controllers.eliminarProducto import eliminarProductoBlueprint
from alchemyClasses.producto import db

app = Flask(__name__)
app.register_blueprint(eliminarProductoBlueprint)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://rosa:Rosa123!@localhost:3306/ing_soft'
app.config.from_mapping(
    SECRET_KEY='dev'
)
db.init_app(app)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
