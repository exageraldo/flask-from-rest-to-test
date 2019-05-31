from flask_restful import Resource, reqparse
from flask import request
from models import UserModel
from serializers import UserSchema

from flask_jwt_extended import (
    create_access_token,
    create_refresh_token
)


class User(Resource):
    def get(self):
        return {'msg': 'Gabriela'}, 200
        # return UserModel.get_all_users(), 200

    def post(self):
        data = request.get_json() or {}
        user = UserSchema.model_validate(data)
        if user:
            user.save()
            return 'User created', 200
        return 'User error', 409


class UserLogin(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

    def post(self):
        data = self.parser.parse_args()
        username = data['username']
        password = data['password']

        current_user = UserModel.find_by_credential(identity=username)
        if not current_user:
            return {'msg': 'User {} doesn\'t exist'.format(username)}, 401
        if UserModel.verify_hash(data['password'], current_user.password):
            access_token = create_access_token(
                identity=username)
            refresh_token = create_refresh_token(
                identity=username)

            response = {'msg': 'Logged in as {}'.format(
                current_user.username), 'token:': access_token}

            set_access_cookies(response, access_token)
            set_refresh_cookies(response, refresh_token)

            return response, 200
        else:
            return {'msg': 'Wrong credentials'}, 401
