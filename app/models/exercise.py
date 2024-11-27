from .. import db

class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    academy_id = db.Column(db.Integer)
    name = db.Column(db.String(50))
    description = db.Column(db.String(256))

    def to_dict(self):
        return{
            'id': self.id,
            'academy_id': self.academy_id,
            'name': self.name,
            'description': self.description
        }