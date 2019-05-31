from main import db
from hashlib import sha256, sha1
from mongoengine.queryset.visitor import Q
from flask_mongoengine import Document
from mongoengine import StringField, ObjectIdField


class UserModel(Document):
    _id = ObjectIdField(required=False)
    username = StringField(
        max_length=120,
        required=True,
        unique=True
    )
    email = StringField(
        max_length=120,
        required=True,
        unique=True
    )

    @staticmethod
    def generate_hash(password):
        return sha1(password.encode('utf-8')).hexdigest()

    @staticmethod
    def verify_hash(password, hash):
        return sha1(password.encode('utf-8')).hexdigest() == hash

    @staticmethod
    def find_by_credential(identity):
        current_user = UserModel.objects(
            Q(username=identity) | Q(email=identity)).first()
        return current_user

    def to_dict(self):
        return {
            "username": self.username,
            "email": self.email
        }

    @classmethod
    def get_all_users(cls):
        all_users = cls.object
        return [user.to_dict() for user in all_users]
