# http://flask.pocoo.org/docs/1.0/config/
import os

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True 

    JWT_TOKEN_LOCATION=['headers']
    JWT_ACCESS_TOKEN_EXPIRES=20
    JWT_REFRESH_TOKEN_EXPIRES=1800
    SECRET_KEY = 'fl4sk-grupI'

class ProductionConfig(Config):
    DEBUG = False

    # MONGO
    MONGODB_DB = 'flask-grupy-prod'
    MONGODB_HOST = 'localhost'
    MONGODB_PORT = 27017

class DevelopmentConfig(Config):
    TESTING = True 
    DEBUG = True

    # MONGO
    MONGODB_DB = 'flask-grupy-dev'
    MONGODB_HOST = 'localhost'
    MONGODB_PORT = 27017
    #MONGODB_USERNAME = 'flask'
    #MONGODB_PASSWORD = 'grupy' 


class TestingConfig(Config):
    TESTING = True 
    DEBUG = False

    # MONGO
    MONGODB_HOST = 'mongomock://localhost'

config = {
    "development": "config.DevelopmentConfig",
    "test": "config.TestingConfig",
    "production": "config.ProductionConfig",
    "default": "config.DevelopmentConfig"
}

def configure_app(app):
    config_name = os.getenv('FLASK_ENV', 'test')
    app.config.from_object(config[config_name])