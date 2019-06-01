from flask import Flask
from flask_restful import Api
from flask_cors import CORS 
from flask_jwt_extended import JWTManager
from flask_mongoengine import MongoEngine
from config import configure_app

app = Flask(__name__)
CORS(app)
configure_app(app)
db = MongoEngine(app)
api = Api(app)
jwt = JWTManager(app)

from resources import User, UserLogin, Users

api.add_resource(
    User,
    '/user',
    '/user/<string:username>'
)

api.add_resource(
    Users,
    '/users'
)

api.add_resource(
    UserLogin,
    '/login'
)
