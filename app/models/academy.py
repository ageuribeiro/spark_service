from .. import db


class Academy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    address = db.Column(db.String(256))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(50))
    incr = db.Column(db.String(30))
    cnpj = db.Column(db.String(20))

    def to_dict(self):
        return{
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'phone': self.phone,
            'email': self.email,
            'incr': self.incr,
            'cnpj': self.cnpj
        
        }