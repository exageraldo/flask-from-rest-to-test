from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_cors import CORS

from flask_mongoengine import MongoEngine


app = Flask(__name__)
CORS(app)
app.config.from_pyfile('config.py')
db = MongoEngine(app)
# db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)
migrate = Migrate(app, db)

from resources import User

api.add_resource(
    User,
    '/user/'
)