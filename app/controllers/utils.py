from flask import jsonify
from functools import wraps
from marshmallow import Schema, fields, ValidationError, validate
import logging

def error_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValidationError as err: # Erros de validação Mashmellows
            return jsonify(err.messages), 400 # for Bad Request
        except ValueError as e:
            return jsonify({'error': str(e), "status_code": 400}), 400 # Bad request
        except AttributeError as e:
            return jsonify({'error': str(e), "status_code": 422}), 422 # Unproccessable Entity
        except KeyError as e:
            return jsonify({'error': f"Missing key: {e}","status_code": 400}), 400
        except TypeError as e:
            return jsonify({'error': str(e), "status_code": 400}), 400
        except Exception as e:
            logging.exception("Erro durante a execução da requisição")
            return jsonify({'error': 'Erro interno do servidor', "status_code": 500}), 500 # Internal Server Error
        


# Schemas de Validação dos models
class PersonSchema(Schema):
    nome = fields.Str(required=True)
    idade = fields.Str(required=True, validate=lambda n: n > 0)
    email = fields.Email(required=True)

class AcademySchema(Schema):
    nome = fields.Str(required=True)
    endereco = fields.Str(required=True)
    tel = fields.Str(required=True)
    email = fields.Email(required=True)

class AccessLogSchema(Schema):
    IdPerson = fields.Int(required=True)
    IdAcademy = fields.Int(required=True)

class ExcerciseSchema(Schema):
    IdAcademy = fields.Int(required=True)
    Name = fields.Str(required=True)

class FinancialSchema(Schema):
    IdPerson = fields.Int(required=True)
    IdAcademy = fields.Int(required=True)
    Amount = fields.Decimal(required=True)
    Status = fields.Str(required=True)

class MembershipSchema(Schema):
    IdPerson = fields.Int(required=True)
    IdAcademy = fields.Int(required=True)
    Start = fields.Time(required=True)
    End = fields.Time(required=True)
    Status = fields.Str(required=True)

class TicketSchema(Schema):
    Desc = fields.Str(required=True)
    Status = fields.Str(required=True)