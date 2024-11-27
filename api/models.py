from . import db

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    academy_id = db.Column(db.Integer)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    birthday = db.Column(db.Date)
    address = db.Column(db.String(256))

class Academy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    address = db.Column(db.String(256))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(50))
    incr = db.Column(db.String(30))
    cnpj = db.Column(db.String(20))

class AccessLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer)
    academy_id = db.Column(db.Integer)
    entry_time = db.Column(db.Time)
    exit_time = db.Column(db.Time)

class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    academy_id = db.Column(db.Integer)
    name = db.Column(db.String(50))
    description = db.Column(db.String(256))
    
class Financial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer)
    academy_id = db.Column(db.Integer)
    amount = db.Column(db.Float)
    pay_status = db.Column(db.Text)

class  Membership(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer)
    academy_id = db.Column(db.Integer)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    membership_status = db.Column(db.Text)

class TrainingExercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    training_plan_id = db.Column(db.Integer)
    academy_id = db.Column(db.Integer)
    exercise_id = db.Column(db.Integer)
    sets = db.Column(db.Integer)
    reps = db.Column(db.Integer)
    weight = db.Column(db.Float)
    duration = db.Column(db.Time)
    
class TrainingPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer)
    academy_id = db.Column(db.Integer)
    name = db.Column(db.String(50))
    description = db.Column(db.String(256))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    email = db.Column(db.String(50))
    data_joined = db.Column(db.Date)

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