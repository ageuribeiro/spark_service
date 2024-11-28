from flask import Blueprint, request, jsonify
from ..models import Membership
from app import db


membership_bp = Blueprint('membership_bp', __name__)

@membership_bp.route('/membership', methods=['GET','POST'])
def handle_memberships():
    if request.method == 'GET':
        memberships = Membership.query.all()
        return jsonify([membership.to_dict() for membership in memberships]), 200
    
    if request.method == 'POST':
        try:
            data = request.get_json()
            membership = membership(**data)
            db.session.add(membership)
            db.session.commit()
            return jsonify(membership.to_dict()), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500