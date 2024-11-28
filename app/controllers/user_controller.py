from flask import Blueprint, request, jsonify
from ..models import User
from app import db


user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/user', methods=['GET','POST'])
def handle_users():
    if request.method == 'GET':
        users = User.query.all()
        return jsonify([user.to_dict() for user in users]), 200
    
    if request.method == 'POST':
        try:
            data = request.get_json()
            user = user(**data)
            db.session.add(user)
            db.session.commit()
            return jsonify(user.to_dict()), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500