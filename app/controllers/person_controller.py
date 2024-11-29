from .utils import error_handler, PersonSchema
from flask import Blueprint, render_template, request, jsonify
from ..models import Person
from app import mongo_db

person_bp = Blueprint('person_bp', __name__)

@person_bp.route('/person', methods=['GET','POST'], endpoint='handle_persons_api')
@error_handler
def handle_persons():
    
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

@person_bp.route('/persons', methods=['GET','POST'], endpoint='persons_page')
def persons_page():
    return render_template('persons.html')