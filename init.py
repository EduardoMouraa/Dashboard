from flask import Flask
import flask_sqlalchemy


from models import db
from decouple import config

POSTGRES_USER=config('POSTGRES_USER', str)
POSTGRES_PASSWORD=config('POSTGRES_PASSWORD', str)
POSTGRES_HOST=config('POSTGRES_HOST', str)
POSTGRES_PORT=config('POSTGRES_PORT', int)
POSTGRES_DB=config('POSTGRES_DB', str)

SQLALCHEMY_TRACK_MODIFICATIONS= config("SQLALCHEMY_TRACK_MODIFICATIONS", bool)

def create_app():
    flask_app = Flask(__name__)
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://{}:{}@{}:{}/{}".format(POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_PORT, POSTGRES_DB)
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.app_context().push()
    db.init_app(flask_app)
    db.create_all()

    return flask_app
