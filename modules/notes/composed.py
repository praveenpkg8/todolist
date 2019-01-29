from models.todo import Notes


def fetch_all_notes():
    notes = list()
    active_notes = Notes.view_all()
    for note in active_notes:
        if note.is_active == True:
            final_content = {
                'id': note.id,
                'content': note.content,
                'created_by': note.created_by,
                'is_active': note.is_active
            }
            notes.append(final_content)

    return notes
