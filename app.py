from database import db
from flask import Flask
from flask_migrate import Migrate
from endpoints import root


def create_app():
    app = Flask(__name__)
    app.register_blueprint(root)
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
    db.init_app(app)
    return app


def setup_database(app):
    migrate = Migrate(app, db)


db = db
app = create_app()
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run()
