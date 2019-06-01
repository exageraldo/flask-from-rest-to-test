# Flask: do Rest ao Test

Esse material leva em consideração que você já saiba os conceitos básicos de Python. Será dada uma introdução ao microframework Flask e mostrado alguns plugins complementares para levantar seu primeiro sistema web completo.

## Flask
Segundo a própria documentação:

> Flask é um microframework para Python baseado em Werkzeug, Jinja2 e
> boas intenções.

Um **microframework** é um termo usado para se referir a estruturas de aplicações web minimalistas.

Para instalar basta digitar (preferencialmente dentro de uma virtualenv):

    pip install Flask
Agora o `hello world` no flask:
```python
# server.py
from flask import Flask 

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, World!'
```
E para rodar o servidor:
```bash
$ export FLASK_APP=hello.py
$ flask run
```

## Flask-Restful
O Flask-RESTful é uma extensão do Flask que adiciona suporte para a construção rápida e prática de APIs REST.

```
pip install flask-restful
```
Agora vamos transformar tudo em Rest!

```python
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')
```

## JSON Web Token
**JWT (JSON Web Token)** é um sistema de transferência de dados que pode ser enviado via POST ou em um cabeçalho HTTP (header) de maneira “segura”, essa informação é assinada digitalmente por um algoritmo HMAC, ou um par de chaves pública/privada usando RSA.

## Flask-JWT-Extended
```
pip install flask-jwt-extended
```
```python
from flask import Flask
from flask_restful import Resource, Api
from flask_jwt_extended import (
    JWTManager, jwt_required
)

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
api = Api(app)
jwt = JWTManager(app)

class HelloWorld(Resource):
    @jwt_required
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')
```
Usamos `jwt_required` para proteger uma rota, tudo o que precisamos fazer é enviar o JWT com a requisição. Por padrão, isso é feito pelo cabeçalho, que tem que ser enviado no seguitne modelo:
```
Authorization: Bearer <access_token>
```
