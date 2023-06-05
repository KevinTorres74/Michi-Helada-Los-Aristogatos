from flask import Flask

from controllers.ConsultaCliente import consultaclienteBlueprint

app = Flask(__name__)

app.register_blueprint(consultaclienteBlueprint)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root: Jimmypage1970@localhost:3306/bdd-ingsoft'
app.config.from_mapping(
    SECRET_KEY='dev'
)
db.init_app(app)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
