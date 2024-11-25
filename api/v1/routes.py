from flask import Blueprint, request, jsonify
from ..models import Tickets, db
from ..controllers import whatsapp_reply
import logging

api_v1 = Blueprint("api_v1", __name__)

@api_v1.route("/create_ticket", methods=["GET", "POST"])
def tickets():
    if request.method == "GET":
        tickets = Tickets.query.all()
        return jsonify([ticket.to_dict() for ticket in tickets])
    
    if request.method == "POST":
        data = request.get_json()
        new_ticket = Tickets(descr=data['descricao'], status='open')
        db.session.add(new_ticket)
        db.session.commit()
        return jsonify(new_ticket.to_dict()), 201
    
@api_v1.route("/whatsapp", methods=['POST'])
def whatsapp_webhook():
    return whatsapp_reply()