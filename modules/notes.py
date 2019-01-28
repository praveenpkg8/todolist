import functools
import json

from flask import Blueprint, request, jsonify

from models.todo import Notes
from status_code import Staus_code

bp = Blueprint('notes', __name__, url_prefix='/notes')


@bp.route('/list', methods=['GET'])
def view():
    active_notes = Notes.query.all()
    data = list()
    for note in active_notes:
        final_content = {
            'id': note.id,
            'content': note.content,
            'created_by': note.created_by,
            # 'created_on': note.created_on,
            'is_active': note.is_active
        }
        data.append(final_content)
    message = {
        "notes": data
    }
    return json.dumps(obj=message), Staus_code.HTTP_200_OK


@bp.route('/view/<int:note_id>', methods=['GET'])
def view_one(note_id):
    note = Notes.view_by_id(note_id)
    # return json.dumps(obj={'content': note.content, 'created_by': note.created_by,  'is_active': note.is_active}), status.HTTP_200_OK

    try:
        return json.dumps(obj={'content': note.content, 'created_by': note.created_by,
                               'is_active': note.is_active}), Staus_code.HTTP_200_OK
    except:
        return 'Improper id provided'


@bp.route('/save', methods=['PUT'])
def save():
    try:
        created_by = request.json['created_by']
        content = request.json['content']
    except:
        return 'No proper inputs are provided'
    final_content = Notes(created_by, content)
    try:
        Notes.add(final_content)
        Notes.commit()
        return 'Note created succesfully', Staus_code.HTTP_201_CREATED

    except:
        return 'problem in adding and commiting DataBase'


@bp.route('/update/<int:note_id>', methods=['PUT'])
def update(note_id):
    note = Notes.view_by_id(note_id)
    try:
        note.content = request.json['content']
    except:
        return 'no proper content provide, check for content attribute', Staus_code.HTTP_406_NOT_ACCEPTABLE
    try:
        Notes.commit()
        return "Note have been updated succesfully", Staus_code.HTTP_202_ACCEPTED

    except:
        return 'problem in commiting to DataBase'


@bp.route('/delete/<int:note_id>', methods=['DELETE'])
def delete(note_id):
    note = Notes.view_by_id(note_id)
    if note is None:
        return 'invalid id'
    else:
        note.is_active = False

        try:
            Notes.commit()
            return "Note have been Deleted succesfully", Staus_code.HTTP_202_ACCEPTED

        except:
            return 'problem in commiting to DataBase'
