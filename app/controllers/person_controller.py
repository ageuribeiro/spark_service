from flask import Blueprint, render_template, request, jsonify
from ..models import Person
from app import mongo_db

person_bp = Blueprint('person_bp', __name__)

@person_bp.route('/person', methods=['GET','POST'])
def handle_persons():
    
    persons_collections = mongo_db.get_collection('person')

    if request.method == 'GET':
        try:
            persons = list(persons_collections.find())
            return jsonify(persons), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    if request.method == 'POST':
        try:
            data = request.get_json()
            persons_collections.insert_one(data)
            
            return jsonify(data), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500

@person_bp.route('/persons', methods=['GET','POST'])
def persons_page():
    return render_template('persons.html')