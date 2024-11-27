from .. import db

class AccessLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer)
    academy_id = db.Column(db.Integer)
    entry_time = db.Column(db.Time)
    exit_time = db.Column(db.Time)

    def to_dict(self):
        return{
            'id': self.id,
            'person_id': self.person_id,
            'academy_id': self.academy_id,
            'entry_time': self.entry_time,
            'exit_time': self.exit_time
        }
        