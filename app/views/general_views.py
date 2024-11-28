from flask import Blueprint, render_template

general_bp = Blueprint('general', __name__)

@general_bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')