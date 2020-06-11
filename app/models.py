from app import db

class Location(db.Model):
    city = db.Column(db.String(24), index=True)
    state = db.Column(db.String(24), index=True)
    mood = db.Column(db.String(140))
    
    def __repr__(self):
        return '<User {}>'.format(self.username)
    