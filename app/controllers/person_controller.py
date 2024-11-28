from flask import Blueprint, request, jsonify
from ..models import Person
from app import db


person_bp = Blueprint('person_bp', __name__)

@person_bp.route('/person', methods=['GET','POST'])
def handle_persons():
    if request.method == 'GET':
        persons = Person.query.all()
        return jsonify([person.to_dict() for person in persons]), 200
    
    if request.method == 'POST':
        try:
            data = request.get_json()
            person = Person(**data)
            db.session.add(person)
            db.session.commit()
            return jsonify(person.to_dict()), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500