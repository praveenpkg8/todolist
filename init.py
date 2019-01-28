import os
import json
import yaml
from flask import Flask, request, jsonify

from flask_api import status
from modules import notes
from models import db





def init_app():
    app = Flask(__name__)
    config = yaml.load(open('config.yaml'))
    app.config['SQLALCHEMY_DATABASE_URI'] = config['SQLALCHEMY_DATABASE_URI']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config['SQLALCHEMY_TRACK_MODIFICATIONS']
    db.init_app(app)
    app.register_blueprint(notes.bp)
    return app


