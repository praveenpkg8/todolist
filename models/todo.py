import datetime
from models import db
import logging


logger = logging.getLogger(__name__)


class Notes(db.Model):

    __tablename__ = 'notes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_by = db.Column(db.String(50))
    content = db.Column(db.String(200))
    created_on = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    is_active = db.Column(db.Boolean())

    def __init__(self, created_by, content):
        self.created_by = created_by
        self.content = content
        self.is_active = True

    def __repr__(self):
        return "<Notes {}".format(self.content)

    @staticmethod
    def get_all_notes():
        notes = Notes.query.all()
        return notes

    @staticmethod
    def get_note(id):
        note = Notes.query.get(id)
        return note

    @staticmethod
    def create_note(note: object):
        db.session.add(note)
        db.session.commit()

    @staticmethod
    def update_note():
        db.session.commit()

