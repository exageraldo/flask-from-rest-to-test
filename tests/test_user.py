import unittest
from main import app
from models import UserModel
from bson import ObjectId

app.config['FLASK_ENV'] = 'test'

user = {
    '_id': ObjectId(), 
    'username': 'lucas',
    'email': 'lucas@gmail.com',  
    'password': UserModel.generate_hash('123')
}
UserModel.objects._collection.insert(user)


class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_users(self):
        response = self.app.get('/users')
        assert response.status_code == 200
        assert len(response.get_json()) == 1
        assert response.status_code == 200

    def test_get_user(self): 
        response = self.app.get('/user/lucas')
        assert response.status_code == 200

    def test_get_user_not_found(self):
        response = self.app.get('/user/ana')
        assert response.status_code == 404

    def test_user_password_valid(self):
        user = UserModel.find_by_credential('lucas@gmail.com')
        self.assertTrue(UserModel.verify_hash("123", user.password))

    def test_user_password_invalid(self):
        user = UserModel.find_by_credential('lucas@gmail.com')
        self.assertFalse(UserModel.verify_hash("1234", user.password))
        self.assertFalse(UserModel.verify_hash(user.password, "1234"))

    def test_user_data(self):
        user_ = UserModel.find_by_credential('lucas@gmail.com')
        self.assertEqual(user.get('username'), user_.username)  