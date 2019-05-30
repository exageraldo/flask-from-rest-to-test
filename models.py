from main import db


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