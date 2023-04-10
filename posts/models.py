from app import db
from sqlalchemy import func


class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String(280))
    location = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=db.func.now())


    def __init__(self, text, location):
        self.text = text
        self.location = location

    def save(self):
        db.session.add(self)
        db.session.commit()

    