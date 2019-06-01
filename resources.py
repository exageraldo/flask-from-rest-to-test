from flask_restful import Resource, reqparse
from flask import request
from models import UserModel

from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    create_refresh_token,
    set_access_cookies,
    set_refresh_cookies,
    jwt_required
)


class Users(Resource):
    @jwt_required
    def get(self):
        return UserModel.get_all_users(), 200


class User(Resource):
    def get(self, username):
        user = UserModel.find_by_credential(identity=username)
        if not user:
            return {'msg': 'User Not Found'}, 404
        return {'user': user.email}, 200

    def post(self):
        data = request.get_json() or {}
        user = UserModel(
            username=data['username'],
            email=data['email'],
            password=UserModel.generate_hash(data['password']))
        if user:
            user.save()
            return {'msg': 'User created'}, 200
        return {'msg': 'User error'}, 409


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

            msg = {'msg': 'Logged in as {}'.format(
                current_user.username), 'token:': access_token}
            return msg, 200
        else:
            return {'msg': 'Wrong credentials'}, 401
