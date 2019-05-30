from main import db
from hashlib import sha256, sha1
from mongoengine.queryset.visitor import Q


class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def to_dict(self):
        return {
            "username": self.username,
            "email": self.email
        }


    @classmethod
    def add_user(cls, username, email):
        db.session.add(
            cls(
                username=username,
                email=email
            )
        )
        db.session.commit()
    
    @classmethod
    def get_all_users(cls):
        all_users = cls.query.all()
        return [user.to_dict() for user in all_users]

    @staticmethod
    def generate_hash(password):
        return sha1(password.encode('utf-8')).hexdigest()

    @staticmethod
    def verify_hash(password, hash):
        return sha1(password.encode('utf-8')).hexdigest() == hash

    @staticmethod
    def find_by_credential(identity):
        current_user = User.objects(
            Q(username=identity) | Q(email=identity)).first()
        return current_user
