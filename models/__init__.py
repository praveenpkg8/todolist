import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()

from models.todo import Notes
from models.registration import UserCredentials