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


class AuthTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_login(self):
        data = {'username': user.get(
            'username'), 'password': '123'}
        response = self.app.post('/login', json=data)

        msg = 'Logged in as {}'.format(user.get('username'))
        assert msg == response.json.get('msg')
        assert 200 == response.status_code

    def test_wrong_login(self):
        data = {'username': 'error', 'password': '123'}
        response = self.app.post('/login', json=data)

        msg = "User error doesn't exist"
        assert msg == response.json.get('msg')
        assert 401 == response.status_code

    def test_headers_access(self):
        data = {'username': user.get(
            'username'), 'password': '123'}
        response = self.app.post('/login', json=data)
        data = response.get_json() 

        access_headers = {'Authorization': 'Bearer {}'.format(data.get('token'))}
        response = self.app.get('/users', headers=access_headers)
        assert response.status_code == 200

    def test_missing_headers(self):
        response = self.app.get('/users')
        assert response.status_code == 401
        assert response.get_json() == {'msg': "Missing Authorization Header"}
