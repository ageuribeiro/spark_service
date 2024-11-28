from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    email = db.Column(db.String(50))
    data_joined = db.Column(db.Date)

    def to_dict(self):
        return{
            'id': self.id,
            'person_id': self.person_id,
            'username': self.username,
            'password': self.password,
            'email': self.email,
            'data_joined': self.data_joined
        }