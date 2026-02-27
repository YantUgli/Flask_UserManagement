from app.repositories.user_repository import UserRepository

class UserServices:
    
    @staticmethod
    def create_user(data):

        if not data.get('name') or not data.get('email'):
            raise ValueError("Name and email are required")
        
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
    
    @staticmethod
    def update_user(user_id, data):
        user = UserRepository.get_user_by_id(user_id)
        print("DATA MASUK:", data)
        print("USER SEBELUM SAVE:", user)
        if not user:
            raise ValueError("user Not found")
        
        if "name" in data:
            if not data["name"]:
                raise ValueError("name cannot be empty")
            user.name = data["name"]

        if "email" in data:
            if not data["email"]:
                raise ValueError("email cannot be empty")
            user.email = data["email"]

        return UserRepository.update_user(user)