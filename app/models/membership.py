from .. import db

class  Membership(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer)
    academy_id = db.Column(db.Integer)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    membership_status = db.Column(db.Text)

    def to_dict(self):
        return{
            'id': self.id,
            'person_id': self.person_id,
            'academy_id': self.academy_id,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'membership_status': self.membership_status
        }
        