from typing import List
from flask import request
from models.todo import Notes
from util.exceptions import (RecordNotFoundException, NoteNotFoundException,
                             NoteDeletedException)
from util.helper import (Dictnote, Listnote)


def fetch_all_notes() -> List:
    all_todo = Notes.get_all_notes()
    if all_todo is not None:
        data = []
        for note in all_todo:
            final_note = Dictnote(
                created_by=note.created_by,
                content=note.content,
                created_at=str(note.created_on),
                is_active=note.is_active
            )
            data.append(final_note)
        return data
    else:
        raise RecordNotFoundException("Records not Found")


def fetch_note(note_id) -> List:
    note = Notes.get_note(note_id)
    if note is not None:
        final_note = Listnote(
            created_by=note.created_by,
            content=note.content,
            created_on=str(note.created_on)
        )
        return final_note
    else:
        raise NoteNotFoundException("Note not Found")
    return note


def save_todo_note():
    note = request.get_json()
    created_by = note['created_by']
    content = note['content']
    note = Notes(created_by, content)
    Notes.create_note(note)


def update_todo_note(note_id: int):
    note = request.get_json()
    todo = Notes.get_note(note_id)
    todo.content = note['content']
    todo.created_by = note['created_by']
    Notes.update_note()


def delete_todo_note(note_id: int):
    note = Notes.get_note(note_id)
    if note is not None:
        if note.is_active is True:
            note.is_active = False
            Notes.update_note()
        else:
            raise NoteDeletedException("Note is already Deleted")
    else:
        raise NoteNotFoundException("Note not Found")
