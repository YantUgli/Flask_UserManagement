from app.extensions import db
from app.models.task_model import Task
from app.models.user_model import User

class TaskRepository:
    @staticmethod
    def get_all_task():
        return Task.query.all()
    
    @staticmethod
    def create_task(data):
        task = Task(
            title = data['title'],
            description = data['description'],
            # status = data['status'],
            user_id = data['user_id'],
        )

        db.session.add(task)
        db.session.commit()
        return task
    
    @staticmethod
    def check_user(user_id):
        user_exists = User.query.get(user_id)

        return user_exists
    
    @staticmethod
    def get_task_by_id(task_id):
        return Task.query.get(task_id)
    
    @staticmethod
    def update_task(data):
        db.session.commit()
        return data
    
    @staticmethod
    def delete_task(task):
        db.session.delete(task)
        db.session.commit()

    @staticmethod
    def get_by_user_id(user_id):
        return Task.query.filter_by(user_id=user_id).all()