from .. import db

class TrainingExercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    training_plan_id = db.Column(db.Integer)
    academy_id = db.Column(db.Integer)
    exercise_id = db.Column(db.Integer)
    sets = db.Column(db.Integer)
    reps = db.Column(db.Integer)
    weight = db.Column(db.Float)
    duration = db.Column(db.Time)

    def to_dict(self):
        return{
            'id': self.id,
            'training_plan_id': self.training_plan_id,
            'academy_id': self.academy_id,
            'exercise_id': self.exercise_id,
            'sets': self.sets,
            'reps': self.reps,
            'weight': self.weight,
            'duration': self.duration
        }