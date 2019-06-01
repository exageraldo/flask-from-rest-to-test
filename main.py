from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
# from flask_migrate import Migrate
# from flask_marshmallow import Marshmallow
from flask_cors import CORS 
from flask_jwt_extended import JWTManager
from flask_mongoengine import MongoEngine
from config import configure_app

app = Flask(__name__)
CORS(app)
#app.config.from_pyfile('config.py')
configure_app(app)
db = MongoEngine(app)
# db = SQLAlchemy(app)
# ma = Marshmallow(app)
api = Api(app)
# migrate = Migrate(app, db)
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
