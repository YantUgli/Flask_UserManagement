from app.extensions import db
from app.models.user_model import User

class UserRepository:
    @staticmethod
    def create_user(data):
        user = User(
            name=data["name"],
            email=data["email"]
        )
        db.session.add(user)
        db.session.commit()
        return user
    
    @staticmethod
    def get_all_users():
        return User.query.all()
    
    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)
    
    @staticmethod
    def delete_user(user):
        db.session.delete(user)
        db.session.commit()
