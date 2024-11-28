from flask import Blueprint, request, jsonify
from ..models import Training_exercise
from app import db


training_exercise_bp = Blueprint('training_exercise_bp', __name__)

@training_exercise_bp.route('/training_exercise', methods=['GET','POST'])
def handle_training_exercises():
    if request.method == 'GET':
        training_exercises = Training_exercise.query.all()
        return jsonify([training_exercise.to_dict() for training_exercise in training_exercises]), 200
    
    if request.method == 'POST':
        try:
            data = request.get_json()
            training_exercise = training_exercise(**data)
            db.session.add(training_exercise)
            db.session.commit()
            return jsonify(training_exercise.to_dict()), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500