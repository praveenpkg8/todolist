from typing import Dict, Any

from models.todo import Notes


def fetch_all_notes() -> list:
    notes = list()
    active_notes = Notes.view_all_note()
    for note in active_notes:
        if note.is_active:
            final_content: Dict[str, Any] = {
                'id': note.id,
                'content': note.content,
                'created_by': note.created_by,
                'is_active': note.is_active
            }
            notes.append(final_content)

    return notes

construct_response_message = lambda **kwargs: kwargs
