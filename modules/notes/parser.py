from typing import List, Dict
from models.todo import Notes
from util.exceptions import UserNameNotFoundException, ContentNotFoundException


class NoteParser:
    @staticmethod
    def note_parse(note: Dict) -> object:
        created_by = note['created_by']
        content = note['content']
        Notes(created_by, content)
        if created_by is None:
            raise UserNameNotFoundException("No Name Found")
        elif content is None:
            raise ContentNotFoundException("No content Found")
        else:
            return Notes

