import datetime
from models import db
import logging
from flask import request
from util.exceptions import (RecordNotFoundException, NoteNotFoundException,
                             NoteDeletedException, DataBaseSessionException)

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
    def view_all_note():
        notes = Notes.query.all()
        if notes is not None:
            return notes
        else:
            raise RecordNotFoundException("Records not Found")

    @staticmethod
    def view_by_id(note_id: int):
        note = Notes.query.get(note_id)
        if note is not None:
            return note
        else:
            raise NoteNotFoundException("Note not found, check with id")

    @staticmethod
    def update_note(note_id: int):
        try:
            note = Notes.query.get(note_id)
            if note is not None:
                request_note = request.get_json()
                note.content = request_note['content']
                db.session.commit()
            else:
                raise NoteNotFoundException("Note not found, check with id")
        except DataBaseSessionException:
            raise DataBaseSessionException("Database Session Error")

    @staticmethod
    def delete_note_check(note_id: int):
        try:
            note = Notes.query.get(note_id)
            if note is None:
                raise NoteNotFoundException("Note not found, check with id")
            elif note.is_active is not False:
                note.is_active = False
                db.session.commit()
            else:
                raise NoteDeletedException("Note is been Deleted already")

        except DataBaseSessionException:
            raise DataBaseSessionException("Database Session Error")

    @staticmethod
    def create_note(note: object):
        try:
            db.session.add(note)
            db.session.commit()

        except DataBaseSessionException:
            raise DataBaseSessionException("Database Session Error")

