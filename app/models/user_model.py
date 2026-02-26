from app.extensions import db
from datetime import datetime

class User(db.Model):
    _tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True )
    name = db.Column(db.String(100), primary_key=False )
    email = db.Column(db.String(120), primary_key=False, unique=True )
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'user {self.email}'
