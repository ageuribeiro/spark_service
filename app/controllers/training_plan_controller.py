from flask import Blueprint, request, jsonify
from ..models import Training_plan
from app import db


training_plan_bp = Blueprint('training_plan_bp', __name__)

@training_plan_bp.route('/training_plan', methods=['GET','POST'])
def handle_training_plans():
    if request.method == 'GET':
        training_plans = Training_plan.query.all()
        return jsonify([training_plan.to_dict() for training_plan in training_plans]), 200
    
    if request.method == 'POST':
        try:
            data = request.get_json()
            training_plan = training_plan(**data)
            db.session.add(training_plan)
            db.session.commit()
            return jsonify(training_plan.to_dict()), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500