from flask import Blueprint, render_template, jsonify
import os
import json

log_bp = Blueprint('log_bp', __name__)

@log_bp.route('/logs')
def display_logs():
    logs_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'--', 'logs','app.json')
    logs = []

    if os.path.exists(logs_path):
        with open(logs_path, 'r') as file:
            logs = json.load(file)

    return render_template('logs.html', logs=logs)