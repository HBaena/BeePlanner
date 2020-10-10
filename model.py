from settings import db


class User(db.Model):
    """docstring for User"""
    username = db.Column(db.Integer, nullable=False, primary_key=True)
    last_name = db.Column(db.String(25), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    phone = db.Column(db.String(10), nullable=False)
    password = db.Column(db.String(25), nullable=False)
    

    # db.relationship must be in the parent table
    activity = db.relationship('Activity', backref='user')


class Activity(db.Model):
    
    activity_id = db.Column(db.Integer, nullable=False, primary_key=True)
    title = db.Column(db.String(25), nullable=False)
    description = db.Column(db.String(300), nullable=False)
    priority = db.Column(db.Integer, nullable=False)
    
    user_id = db.Column(db.Integer, db.ForeignKey(
        'user.user_id'), nullable=False)

    location = db.Column(db.String(50), nullable=False)

    schedule = db.relationship('Schedule', backref='activity')
    reminder = db.relationship('Reminder', backref='activity')
    note = db.relationship('Note', backref='activity')



class Schedule(db.Model):

    schedule_id = db.Column(db.Integer, nullable=False, primary_key=True)
    activity_id = db.Column(db.Integer, db.ForeignKey(
        'activity.activity_id'), nullable=False, primary_key=True)
    time_init = db.Column(db.DateTime, nullable=False, primary_key=True)
    time_finish = db.Column(db.DateTime, nullable=False, primary_key=True)
    day = db.Column(db.String(10), nullable=False, primary_key=True)
    



class Note(db.Model):

    note_id = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    description = db.Column(db.String(30), nullable=False, )
    note_date = db.Column(db.DateTime, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False)
    modified_date = db.Column(db.DateTime, nullable=False)
    activity_id = db.Column(db.Integer, db.ForeignKey(
        'activity.activity_id'), nullable=False)
