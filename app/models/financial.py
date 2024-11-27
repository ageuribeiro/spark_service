from .. import db

class Financial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer)
    academy_id = db.Column(db.Integer)
    amount = db.Column(db.Float)
    pay_status = db.Column(db.Text)

    def to_dict(self):
        return{
            'id': self.id,
            'person_id': self.person_id,
            'academy_id': self.academy_id,
            'amount': self.amount,
            'pay_status': self.pay_status
        }
        