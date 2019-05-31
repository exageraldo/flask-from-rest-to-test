from main import ma
from models import UserModel


class UserSchema(ma.ModelSchema):
    class Meta:
        model = UserModel
    
    @classmethod
    def model_validate(cls, data):
        serializer = cls()
        if serializer.validate(data):
            return None
        data_serialized = serializer.dump(data).data
        return UserModel(**data_serialized)