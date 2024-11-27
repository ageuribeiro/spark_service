from flask import Blueprint, request, jsonify, render_template
from werkzeug.exceptions import HTTPException
from ..models import db, Person, Academy, AccessLog, Exercise, Financial, Membership, TrainingExercise, TrainingPlan, User, Tickets
from ..controllers import whatsapp_reply
import logging

app = Blueprint("app", __name__)

# Endpoint inicial
@app.route('/')
def home():
    return render_template('index.html')

# Endpoint para tratamento de excessões
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify(code=e.code, name=e.name, description=e.description)
    response.content_type = "application/json"
    return response

# Endpoint para listar as pessoas
@app.route('/persons', methods=['GET', 'POST'])
def persons():
    if request.method == 'GET':
        persons = Person.query.all()
        return jsonify([person.to_dict() for person in persons]), 200
    
    if request.method == 'POST':
        try:
            data=request.get_json()
            new_person = Person(**data)
            db.session.add(new_person)
            db.session.commit()
            logging.info(info=str(data))
            return jsonify(new_person.to_dict()), 201
        except Exception as e:
            logging.error(error=str(e))
            return jsonify(error=str(e)), 500
        
# Endpoint para listar as academias
@app.route('/academies', methods=['GET', 'POST'])
def academies():
    if request.method == 'GET':
        academies = Academy.query.all()
        return jsonify([academy.to_dict() for academy in academies]), 200
    if request.method == 'POST':
        try:
            data=request.get_json()
            new_academy = Academy(**data)
            db.session.add(new_academy)
            db.session.commit()
            logging.info(info=str(data))
            return jsonify(new_academy.to_dict()), 201
        except Exception as e:
            logging.error(error=str(e))
            return jsonify(error=str(e)), 500


# Endpoint para listar os tickets  
@app.route("/create_ticket", methods=["GET", "POST"])
def tickets():
    if request.method == "GET":
        try:
            tickets = Tickets.query.all()
            return jsonify([ticket.to_dict() for ticket in tickets]), 201
        except Exception as e:
            return jsonify(error=str(e)), 500
    
    if request.method == "POST":
        try:

            data = request.get_json()
            new_ticket = Tickets(descr=data['descricao'], status='open')
            db.session.add(new_ticket)
            db.session.commit()
            logging.info(info=str(data, 201))
            return jsonify(new_ticket.to_dict()), 201
        except Exception as e:
            logging.error(error=str(e))
            return jsonify(error=str(e)), 500

# Enpoint para abertura de chamados atraves do WhatsApp
@app.route("/whatsapp", methods=['POST'])
def whatsapp_webhook():
    return whatsapp_reply()