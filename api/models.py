from . import db

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    academy_id = db.Column(db.Integer)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    birthday = db.Column(db.Date)
    address = db.Column(db.String(256))

class Tickets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descr = db.Column(db.String(256))
    status = db.Column(db.String(50))

    def to_dict(self):
        return {
            "id": self.id,
            "descr": self.descr,
            "status": self.status
        }