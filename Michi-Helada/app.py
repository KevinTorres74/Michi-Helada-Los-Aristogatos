from flask import Flask, redirect, url_for
from alchemyClasses.cliente import db
from controllers.register import registerBlueprint

app = Flask(__name__, instance_relative_config=True)
app.register_blueprint(registerBlueprint)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:Josue318#@localhost:3306/prueba"
app.config.from_mapping(
    SECRET_KEY = 'dev'
)
db.init_app(app)

@app.route('/', methods=['GET','POST'])
def hello_world():
    return redirect(url_for('register.register'))

if __name__ == '__main__':
    db.create_all()
    app.run()
