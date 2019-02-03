from typing import List

from flask import request

from models import Notes
from util.exceptions import NoteNotFoundException
from util.helper import Listnote


class TodoParser:
    @staticmethod
    def parse_save_note(note_id):
        try:
            created_by = request.json['created_by']
            content = request.json['content']
        except KeyError:
            raise

        pass



