import os
import json
import yaml
from flask import Flask, request, jsonify

from todo.models import db, Notes
from flask_api import status
from todo import notes




# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/notes'
# db.init_app(app)




app = Flask(__name__)
config = yaml.load(open('config.yaml'))
app.config['SQLALCHEMY_DATABASE_URI'] = config['SQLALCHEMY_DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config['SQLALCHEMY_TRACK_MODIFICATIONS']
db.init_app(app)
app.register_blueprint(notes.bp)
@app.route("/", methods = ["GET"])
def welcome():
    return json.dumps(obj={ "msg" : "welcome to todo app " }), status.HTTP_200_OK









if __name__ == '__main__':
    app.run(debug= True, port = 4500)