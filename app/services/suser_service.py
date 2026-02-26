from app.repositories.user_repository import UserRepository

class UserServices:
    
    @staticmethod
    def create_user(data):

        if not data.get('name') or not data.get('email'):
            return None, "name and email are required"
        
        return UserRepository.create_user(data)
    
    @staticmethod
    def get_all_users():
        return UserRepository.get_all_users()
    
    @staticmethod
    def get_user(user_id):
        return UserRepository.get_user_by_id(user_id)
    
    @staticmethod
    def delete_user(user_id):
        user = UserRepository.get_user_by_id(user_id)
        if not user:
            return None
        
        UserRepository.delete_user(user)
        return user
