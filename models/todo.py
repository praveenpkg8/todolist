from models import db
from datetime import datetime


class Notes(db.Model):

    __tablename__ = 'notes'

    id = db.Column(db.Integer,primary_key = True,  autoincrement = True)
    created_by = db.Column(db.String(50))
    content = db.Column(db.String(200))
    created_on = db.Column(db.String(50))
    is_active = db.Column(db.Boolean())

    def __init__(self, created_by, content):
        self.created_by = created_by
        self.content = content
        self.created_on = str(datetime.utcnow())
        self.is_active = True

    def __repr__(self):
        return "<Notes {}".format(self.content)

    @staticmethod
    def view_all():
        return Notes.query.all()

    @staticmethod
    def view_by_id(note_id):
        return Notes.query.get(note_id)

      
    @staticmethod
    def add(object):
        db.session.add(object)

    @staticmethod
    def commit():
        db.session.commit()







