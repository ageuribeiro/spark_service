from flask import Blueprint, render_template, request, jsonify, abort
from .utils import error_handler, PersonSchema
from app import mongo_db
from bson.objectid import ObjectId
import logging

person_bp = Blueprint('person_bp', __name__)

@person_bp.route('/person', methods=['GET'], endpoint='get_persons')
@error_handler
def get_persons():
    persons_collections = mongo_db.get_collection('persons')
    try:
        persons = list(persons_collections.find())
        return jsonify(persons), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@person_bp.route('/persons/<person_id>', methods=['GET'], endpoint='get_person')
@error_handler
def get_person(person_id):
    persons_collection = mongo_db.get_collection('persons')
    try:
        person =persons_collection.find_one({"_id": ObjectId(person_id)})
        if person:
            return jsonify(person), 200
        else:
            abort(404)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@person_bp.route('/persons', methods=['POST'], endpoint='create_person')
@error_handler
def create_person():
    schema = PersonSchema()
    persons_collections = mongo_db.get_collection('persons')
    try:
        
        data = schema.load(request.get_json())
        result = persons_collections.insert_one(data)
        new_person = persons_collections.find_one({"_id": result.inserted_id})
        return jsonify(new_person), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@person_bp.route('/persons/page', endpoint='persons_page')
def persons_page():
    return render_template('persons.html')