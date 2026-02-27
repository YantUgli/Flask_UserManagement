from app.repositories.task_repository import TaskRepository

class TaskService:
    @staticmethod
    def get_all_task():
        return TaskRepository.get_all_task()
    
    @staticmethod
    def create_task(data):
        if not data.get('title'):
            raise ValueError("title is required")
        
        user_id = data.get('user_id')
        check_user = TaskRepository.check_user(user_id)
        
        if not check_user:
            raise ValueError(f"User dengan id tersebut tidak di temukan")
        
        return TaskRepository.create_task(data)
    
    @staticmethod
    def get_task(task_id):
        return TaskRepository.get_task_by_id(task_id)
    
    @staticmethod
    def update_task(task_id, data):
        task = TaskRepository.get_task_by_id(task_id)

        if not task:
            raise ValueError("task not found")
        
        if "title" in data:
            if not data["title"]:
                raise ValueError('title cannot be empty')
            task.title= data['title']

        if "description" in data:
            task.description = data['description']
        
        if "status" in data:
            task.status = data['status']

        return TaskRepository.update_task(task)
    
    @staticmethod
    def delete_task(task_id):
        task = TaskRepository.get_task_by_id(task_id)
        if not task:
            return None

        TaskRepository.delete_task(task)
        return task
    
    @staticmethod
    def get_tasks_by_user(user_id):
        user = TaskRepository.check_user(user_id)

        if not user:
            return None
        
        return TaskRepository.get_by_user_id(user_id)