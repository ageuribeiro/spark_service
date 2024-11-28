from app import db

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