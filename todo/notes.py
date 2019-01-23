import functools
import json

from flask import Blueprint, request,jsonify

from todo.models import  Notes
from flask_api import status


bp = Blueprint('notes',__name__,url_prefix='/notes')


@bp.route('/viewall', methods=['GET'])
def view():
    active_notes = Notes.query.all()
    data = list()
    for note in active_notes:
        final_content = {
            'id': note.id,
            'content': note.content,
            'created_by': note.created_by,
            'created_on': note.created_on,
            'is_active': note.is_active
        }
        data.append(final_content)
    return json.dumps(obj={'hello': data}), status.HTTP_200_OK 


@bp.route('/view/<int:note_id>', methods=['GET'])
def view_one(note_id):
    note = Notes.view_by_id(note_id)
    try:
        return json.dumps(obj={'content': note.content, 'created_by': note.created_by, 'created_on': note.created_on, 'is_active': note.is_active}), status.HTTP_200_OK
    except:
        return 'Improper id provided'


@bp.route('/save', methods= ['PUT'])
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
        return 'Note created succesfully', status.HTTP_201_CREATED

    except:
        return 'problem in adding and commiting DataBase'

@bp.route('/update/<int:note_id>', methods= ['PUT'])
def update(note_id):
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


@bp.route('/delete/<int:note_id>', methods= ['DELETE'])
def delete(note_id):
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





