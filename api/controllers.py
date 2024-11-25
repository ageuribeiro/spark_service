from flask import request
from twilio.twiml.messaging_response import MessagingResponse
from .models import Tickets, db
from . import mongo_db

def whatsapp_reply():
    msg = request.form.get('Body')
    resp = MessagingResponse()
    resp.message("Chamado Recebido: " + msg)

    # Adicionar o chamado na lista e salvar no SQL Server
    new_ticket = Tickets(descr=msg, status="Aberto")
    db.session.add(new_ticket)
    db.session.commit()

    # Adicionar o log no MongoDB
    log_entry = {"descricao": msg, "status": "Aberto"}
    mongo_db.logs.insert_one(log_entry)

    return str(resp)
