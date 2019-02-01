import json
from flask import Blueprint, request
from modules.notes.composed import fetch_all_notes
from models.todo import (Notes, NoteNotFoundException,
                         logger)
from modules.notes.composed import construct_response_message
from modules.notes.parser import NoteParser
from util.exceptions import (NoteDeletedException, DataBaseSessionException,
                             RecordNotFoundException)
from status import status

bp = Blueprint('notes', __name__, url_prefix='/todo')


@bp.route('/notes', methods=['GET'])
def view():
    try:
        data = fetch_all_notes()
        message = construct_response_message(notes=data)
        return json.dumps(message), status.HTTP_200_OK

    except RecordNotFoundException as e:
        logger.error(msg=e.error_message)
        message = construct_response_message(error_message=e.error_message)
        return json.dumps(message), status.HTTP_404_NOT_FOUND


@bp.route('/notes/<int:note_id>', methods=['GET'])
def view_one(note_id):
    try:
        note = Notes.view_by_id(note_id)
        return json.dumps(
            obj={'content': note.content, 'created_by': note.created_by, 'created_on': str(note.created_on),
                 'is_active': note.is_active}), status.HTTP_200_OK

    except NoteNotFoundException as e:
        logger.error(msg=e.error_message)
        message = construct_response_message(error_message=e.error_message)
        return json.dumps(message), status.HTTP_404_NOT_FOUND


@bp.route('/notes', methods=['PUT'])
def save_note():
    try:
        NoteParser.note_parse()
        message = construct_response_message(message='Note created successfully')
        return json.dumps(message), status.HTTP_201_CREATED

    except DataBaseSessionException as e:
        logger.error(msg=e.error_message)
        message = construct_response_message(error_message=e.error_message)
        return json.dumps(message), status.HTTP_500_INTERNAL_SERVER_ERROR


    except KeyError as err:
        error_message = "Key error missing"
        logger.error(msg=error_message)
        message = construct_response_message(error_message=error_message + str(err))
        return json.dumps(message), status.HTTP_404_NOT_FOUND


@bp.route('/notes/<int:note_id>', methods=['PUT'])
def update_note(note_id):
    try:
        Notes.update_note(note_id)
        message = construct_response_message(message='Note updated successfully')
        return json.dumps(message), status.HTTP_200_OK

    except NoteNotFoundException as e:
        logger.error(msg=e.error_message)
        message = construct_response_message(error_message=e.error_message)
        return json.dumps(message), status.HTTP_404_NOT_FOUND

    except DataBaseSessionException as e:
        logger.error(msg=e.error_message)
        message = construct_response_message(error_message=e.error_message)
        return json.dumps(message), status.HTTP_500_INTERNAL_SERVER_ERROR


@bp.route('/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    try:
        Notes.delete_note_check(note_id)
        message = construct_response_message(response_message="Note Deleted succesfully")
        return json.dumps(message), status.HTTP_200_OK

    except NoteDeletedException as e:
        logger.error(msg=e.error_message)
        message = construct_response_message(error_message=e.error_message)
        return json.dumps(message), status.HTTP_406_NOT_ACCEPTABLE

    except NoteNotFoundException as e:
        logger.error(msg=e.error_message)
        message = construct_response_message(error_message=e.error_message)
        return json.dumps(message), status.HTTP_404_NOT_FOUND

    except DataBaseSessionException as e:
        logger.error(msg=e.error_message)
        message = construct_response_message(error_message=e.error_message)
        return json.dumps(message), status.HTTP_500_INTERNAL_SERVER_ERROR
