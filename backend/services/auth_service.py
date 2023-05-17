from passlib.hash import pbkdf2_sha256
from repositories.user_repository import UserRepository

class AuthService:
    @staticmethod
    def register_user(username, password, role):
        hashed_password = pbkdf2_sha256.hash(password)
        user_id = UserRepository.create_user(username, hashed_password, role)
        return user_id

    @staticmethod
    def login(username, password):
        user = UserRepository.find_user_by_username(username)
        if user and pbkdf2_sha256.verify(password, user.password):
            return user
        return None