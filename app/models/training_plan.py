from .. import db

class TrainingPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer)
    academy_id = db.Column(db.Integer)
    name = db.Column(db.String(50))
    description = db.Column(db.String(256))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)

    def to_dict(self):
        return {
            'id': self.id,
            'person_id': self.person_id,
            'academy_id': self.academy_id,
            'name': self.name,
            'description': self.description,
            'start_date': self.start_date,
            'end_date': self.end_date
        }
        