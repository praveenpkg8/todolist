from typing import List, Dict
from models.todo import Notes
from flask import request


class NoteParser:
    @staticmethod
    def note_parse():
        try:
            request_note = request.get_json()
            created_by = request_note['created_by']
            content = request_note['content']
            final_note = Notes(created_by, content)
            Notes.create_note(final_note)

        except KeyError as err:
            raise err





