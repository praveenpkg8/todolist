import flask_sqlalchemy
from datetime import datetime

db = flask_sqlalchemy.SQLAlchemy()

class Notes(db.Model):

    __tablename__ = 'notes'

    id = db.Column(db.Integer,primary_key = True,  autoincrement = True)
    created_by = db.Column(db.String(50))
    content = db.Column(db.String(200))
    created_on = db.Column(db.DateTime())
    is_active = db.Column(db.Boolean())

    def __init__(self, created_by, content):
        self.created_by = created_by
        self.content = content
        self.created_on = datetime.utcnow()
        self.is_active = True

    def __repr__(self):
        return "<Notes {}".format(self.content)

    @staticmethod
    def view_all():
        try:
            return Notes.query.all()

        except:
            return "No Notes found in DB"

    @staticmethod
    def view_by_id(note_id):
        try:
            return Notes.query.get(note_id)

        except:
            return 'improper id provided'

    @staticmethod
    def add(object):
        db.session.add(object)

    @staticmethod
    def commit():
        db.session.commit()







