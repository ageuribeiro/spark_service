from flask import Blueprint, request, jsonify
from ..models import Financial
from app import db


financial_bp = Blueprint('financial_bp', __name__)

@financial_bp.route('/financial', methods=['GET','POST'])
def handle_financials():
    if request.method == 'GET':
        financials = Financial.query.all()
        return jsonify([financial.to_dict() for financial in financials]), 200
    
    if request.method == 'POST':
        try:
            data = request.get_json()
            financial = financial(**data)
            db.session.add(financial)
            db.session.commit()
            return jsonify(financial.to_dict()), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500