from flask_mongoengine import Document
from mongoengine import StringField, ObjectIdField

class UserModel(Document):
    _id = ObjectIdField(required=False)
    username = StringField(
        max_length=120,
        required=True,
        unique=True
    )
    username = StringField(
        max_length=120,
        required=True,
        unique=True
    )
    
