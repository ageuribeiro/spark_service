from .utils import error_handler, AccessLogSchema
from flask import Blueprint, request, jsonify
from ..models import AccessLog
from app import mongo_db

access_log_bp = Blueprint('access_log_bp', __name__)

@access_log_bp.route('/logs_acesso', methods=['GET','POST'])
@error_handler
def handle_access_logs():

    access_log_collections = mongo_db.get_collection('access_logs')

    if request.method == 'GET':
        try:
            access_logs = list(access_log_collections.find())
            return jsonify(access_logs), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
        
    if request.method == 'POST':
        try:
            schema = AccessLogSchema()
            data = schema.load(request.get_json())
            access_log_collections.insert_one(data)
            
            return jsonify(data), 201
        
        except Exception as e:
            return jsonify({'error': str(e)}), 500
        