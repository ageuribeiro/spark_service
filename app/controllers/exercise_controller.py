from flask import Blueprint, request, jsonify
from ..models import Exercise
from app import db


exercise_bp = Blueprint('exercise_bp', __name__)

@exercise_bp.route('/exercise', methods=['GET','POST'])
def handle_exercises():
    if request.method == 'GET':
        exercises = Exercise.query.all()
        return jsonify([exercise.to_dict() for exercise in exercises]), 200
    
    if request.method == 'POST':
        try:
            data = request.get_json()
            exercise = exercise(**data)
            db.session.add(exercise)
            db.session.commit()
            return jsonify(exercise.to_dict()), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500