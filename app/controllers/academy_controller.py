from flask import Blueprint, request, jsonify
from ..models import Academy
from app import db

academy_bp = Blueprint('academy_bp', __name__)

@academy_bp.route('/academy', methods=['GET','POST'])
def handle_academies():
    if request.method == 'GET':
        academies = Academy.query.all()
        return jsonify([academies.to_dict() for academy in academies]), 200
    
    if request.method == 'POST':
        try:
            data = request.get_json()
            academy = Academy(**data)
            db.session.add(academy)
            db.session.commit()
            return jsonify(academy.to_dict()), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500
