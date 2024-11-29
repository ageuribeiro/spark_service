from flask import Blueprint, render_template, request, jsonify
from .utils import error_handler, PersonSchema
from app import mongo_db
from bson.objectid import ObjectId
import logging
from ..models import Person

person_bp = Blueprint('person_bp', __name__)

@person_bp.route('/person', methods=['GET'], endpoint='get_persons')
@error_handler
def get_persons():
    
    persons_collections = mongo_db.get_collection('persons')

    if request.method == 'GET':
        try:
            persons = list(persons_collections.find())
            return jsonify(persons), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    if request.method == 'POST':
        try:
            schema = PersonSchema()
            data = schema.load(request.get_json())
            persons_collections.insert_one(data)
            
            return jsonify(data), 201
        
        except Exception as e:
            return jsonify({'error': str(e)}), 500

@person_bp.route('/persons/<person_id>', methods=['GET'], endpoint='get_person')
@error_handler
def get_person(person_id):
    return render_template('persons.html')


@person_bp.route('/persons', methods=['POST'], endpoint='create_person')
@error_handler
def create_person():
    return True

@person_bp.route('/persons/page', endpoint='persons_page')
def persons_page():
    return render_template('persons.html')