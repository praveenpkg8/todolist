import json
from flask import Blueprint
from status import Status
from util.exceptions import NoteNotFoundException, NoteDeletedException
from util.helper import construct_response_message
from modules.notes.composed import (fetch_all_notes, fetch_note,
                                    save_todo_note, update_todo_note,
                                    delete_todo_note)

bp = Blueprint('notes', __name__, url_prefix='/todo')


@bp.route('/list', methods=['GET'])
def view_all_todo():
    notes = fetch_all_notes()
    message = construct_response_message(notes=notes)
    return json.dumps(message), Status.HTTP_200_OK


@bp.route('/note/<int:note_id>', methods=['GET'])
def view_note(note_id):
    try:
        note = fetch_note(note_id)
        return json.dumps(obj=note), Status.HTTP_200_OK
    except NoteNotFoundException as e:
        message = construct_response_message(error_message=e.error_message)
        return json.dumps(message), Status.HTTP_404_NOT_FOUND


@bp.route('/note', methods=['PUT'])
def save_note():
    try:
        save_todo_note()
        message = construct_response_message(response_message="Note created Successfully")
        return json.dumps(message), Status.HTTP_404_NOT_FOUND
    except KeyError as err:
        message = construct_response_message(error_message='key error : ' + str(err))
        return json.dumps(message), Status.HTTP_404_NOT_FOUND


@bp.route('/note/<int:note_id>', methods=['PUT'])
def update_note(note_id):
    try:
        update_todo_note(note_id)
        message = construct_response_message(response_message="Note Updated Successfully")
        return json.dumps(message), Status.HTTP_200_OK
    except KeyError as err:
        message = construct_response_message(error_message='key error : ' + str(err))
        return json.dumps(message), Status.HTTP_404_NOT_FOUND


@bp.route('/note/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    try:
        delete_todo_note(note_id)
        message = construct_response_message(response_message="Note Deleted Successfully")
        return json.dumps(message), Status.HTTP_200_OK
    except KeyError as err:
        message = construct_response_message(error_message='key error : ' + str(err))
        return json.dumps(message), Status.HTTP_404_NOT_FOUND
    except NoteNotFoundException as e:
        message = construct_response_message(error_message=e.error_message)
        return json.dumps(message), Status.HTTP_404_NOT_FOUND
    except NoteDeletedException as e:
        message = construct_response_message(error_message=e.error_message)
        return json.dumps(message), Status.HTTP_404_NOT_FOUND
