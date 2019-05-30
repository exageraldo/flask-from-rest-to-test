from flask_restful import Resource
from flask import request
from models import UserModel
from serializers import UserSchema


class User(Resource):
    def get(self):
        return UserModel.get_all_users(), 200
    
    def post(self):
        data = request.get_json() or {}
        user = UserSchema.model_validate(data)
        if user:
            user.save()
            return 'User created', 200
        return 'User error', 409