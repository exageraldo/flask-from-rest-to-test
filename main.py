from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)
migrate = Migrate(app, db)

from resources import User, UserLogin

api.add_resource(
    User,
    '/user/'
)

api.add_resource(
    UserLogin,
    '/login'
)
