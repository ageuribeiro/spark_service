from flask import Blueprint, request, jsonify
from ..models import AccessLog
from app import db

access_log_bp = Blueprint('access_log_bp', __name__)

@access_log_bp.route('/logs_acesso', methods=['GET','POST'])
def handle_access_logs():
    if request.method == 'GET':
        access_logs = AccessLog.query.all()
        return jsonify([access_logs.to_dict() for access_log in access_logs]), 200
    
    if request.method == 'POST':
        try:
            data = request.get_json()
            access_log = AccessLog(**data)
            db.session.add(access_log)
            db.session.commit()
            return jsonify(access_log.to_dict()), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500