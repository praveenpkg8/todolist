from datetime import datetime
from models import db
import logging

logger = logging.getLogger(__name__)



class NoteNotFoundException(Exception):

    def __init__(self, value):
        self.error_message = value

class RecordNotFoundException(Exception):

    def __init__(self, value):
        self.error_message = value






class Notes(db.Model):

    __tablename__ = 'notes'

    id = db.Column(db.Integer, primary_key = True,  autoincrement = True)
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
            notes = Notes.query.all()
            if notes is not None:
                return notes
            else:
                raise RecordNotFoundException("Records not Found")

        except Exception as e:
            logger.error(e)
            raise RecordNotFoundException("Records not Found")

    @staticmethod
    def view_by_id(note_id):
        try:
            note = Notes.query.get(note_id)
            if note is not None:
                return note
            else:
                raise NoteNotFoundException("Note not found, check with id")

        except Exception as e:
            logger.error(e)
            raise NoteNotFoundException("Note not found, check with id")




    @staticmethod
    def add(obj):
        db.session.add(obj)

    @staticmethod
    def commit():
        db.session.commit()







