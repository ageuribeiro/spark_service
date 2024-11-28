from flask import Blueprint, render_template, jsonify, current_app
import logging
import os
import json

log_bp = Blueprint('log_bp', __name__)

@log_bp.route('/logs')
def display_logs():
    logs_collection = current_app.config["LOGS_COLLECTION"]
    logs = list(logs_collection.find())

    return render_template('logs.html', logs=logs)


@log_bp.route('/logs_json', methods=['POST'])
def save_log():
    logs_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '--', 'logs','app.json')
    logs_collection = current_app.config["LOGS_COLLECTION"]

    if os.path.exists(logs_path):
        with open(logs_path, 'r') as log_file:
            for line in log_file:
                try:
                    log_data = json.loads(line)
                    logs_collection.insert_one(log_data)
                except json.JSONDecodeError as e:
                    logging.ERROR(f'Erro ao decodificar JSON: {e}')
                    print(f"Erro ao decodificar JSON: {e}")
                    return jsonify({"message":"Erro ao processar o log", "error":str(e)}), 500

    return jsonify({"message":"logs salvos com sucesso"}), 200