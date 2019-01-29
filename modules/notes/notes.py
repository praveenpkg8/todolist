import functools
import json

from flask import Blueprint, request, jsonify
from modules.notes.composed import fetch_all_notes
from models.todo import Notes
from flask_api import status

bp = Blueprint('notes', __name__, url_prefix='/todo')


@bp.route('/notes', methods=['GET'])
def view():
    data = fetch_all_notes()
    return json.dumps(obj={'notes': data}), status.HTTP_200_OK


@bp.route('/notes/<int:note_id>', methods=['GET'])
def view_one(note_id):
    note = Notes.view_by_id(note_id)
    try:
        return json.dumps(obj={'content': note.content, 'created_by': note.created_by, 'created_on': note.created_on,
                               'is_active': note.is_active}), status.HTTP_200_OK
    except:
        return 'Improper id provided'


@bp.route('/notes', methods=['PUT'])
def save_note():
    try:
        created_by = request.json['created_by']
        content = request.json['content']
    except:
        return 'No proper inputs are provided'
    final_content = Notes(created_by, content)
    try:
        Notes.add(final_content)
        Notes.commit()
        return 'Note created succesfully', status.HTTP_201_CREATED

    except:
        return 'problem in adding and commiting DataBase'


@bp.route('/notes/<int:note_id>', methods=['PUT'])
def update_note(note_id):
    note = Notes.view_by_id(note_id)
    try:
        note.content = request.json['content']

    except:
        return 'no proper content provide, check for content attribute'
    try:
        Notes.commit()
        return "Note have been updated succesfully", status.HTTP_202_ACCEPTED

    except:
        return 'problem in commiting to DataBase'


@bp.route('/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    note = Notes.view_by_id(note_id)
    if note is None:
        return 'invalid id'
    else:
        note.is_active = False

        try:
            Notes.commit()
            return "Note have been Deleted succesfully", status.HTTP_202_ACCEPTED

        except:
            return 'problem in commiting to DataBase'
