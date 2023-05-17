from flask import request
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, get_jwt_identity
)
from flask_restful import Resource
from services.auth_service import AuthService

jwt = JWTManager()

@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.username

class RegisterController(Resource):
    def post(self):
        username = request.json['username']
        password = request.json['password']
        role = request.json['role']
        user_id = AuthService.register_user(username, password, role)
        return {'message': 'User registered successfully', 'user_id': user_id}, 201

class LoginController(Resource):
    def post(self):
        username = request.json['username']
        password = request.json['password']
        user = AuthService.login(username, password)
        if user:
            access_token = create_access_token(identity=user)
            return {'access_token': access_token}, 200
        return {'message': 'Invalid credentials'}, 401