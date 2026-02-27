from app.extensions import db
from datetime import datetime, timezone

class Task(db.Model):
    __tablename__ = "task"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(250))
    status = db.Column(db.String(20), default="pending")
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    # Menghubungkan ke tabel user
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    # Opsional: Mempermudah akses data user dari objek task (misal: task.author)
    author = db.relationship('User', backref=db.backref('tasks', lazy=True))

    def __repr__(self):
        return f'<Task {self.title}>'
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "user_id": self.user_id,
            "created_at": self.created_at.isoformat(), # Convert datetime ke string
            "user": {
                "id": self.author.id,
                "name": self.author.name,
                "email": self.author.email
            } if self.author else None
        }