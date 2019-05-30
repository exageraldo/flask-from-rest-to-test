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

    def to_dict(self):
        return {
            "username": self.username,
            "email": self.email
        }

    @classmethod
    def get_all_users(cls):
        all_users = cls.object
        return [user.to_dict() for user in all_users]
