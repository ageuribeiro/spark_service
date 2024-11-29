from .utils import error_handler, AcademySchema
from flask import Blueprint, render_template, request, jsonify
from ..models import Academy
from app import mongo_db

academy_bp = Blueprint('academy_bp', __name__)

@academy_bp.route('/academy', methods=['GET','POST'])
@error_handler
def handle_academies():

    academies_collections = mongo_db.get_collection(academies)

    if request.method == 'GET':
        try:
            academies = list(academies_collections.find())
            return jsonify(academies), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
        
    if request.method == 'POST':
        try:
            schema = AcademySchema()
            data = schema.load(request.get_json())
            academies_collections.insert_one(data)

            return jsonify(data), 201
        
        except Exception as e:
            return jsonify({'error': str(e)}), 500

@academy_bp.route('/academies', methods=['GET'])
def academies_page():
    return render_template('academies.html')