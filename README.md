[![pipeline status](https://gitlab.com/gabicavalcantesilva/flask-api-ci/badges/master/pipeline.svg)](https://gitlab.com/lucasalveslm/jeanne/commits/master)
[![coverage report](https://gitlab.com/gabicavalcantesilva/flask-api-ci/badges/master/coverage.svg?job=coverage)](https://gitlab.com/lucasalveslm/jeanne/-/jobs/artifacts/master/file/htmlcov/index.html?job=coverage)

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

## CORS

Cross-Origin Resource Sharing (Compartilhamento de recursos com origens diferentes) é um mecanismo que usa cabeçalhos adicionais [HTTP](https://developer.mozilla.org/pt-BR/docs/Glossario/HTTP "A definição do termo (HTTP) ainda não foi escrita; por favor, considere fazer essa contribuição!") para informar a um navegador que permita que um aplicativo Web seja executado em uma origem (domínio) com permissão para acessar recursos selecionados de um servidor em uma origem distinta. Um aplicativo Web executa uma **requisição _cross-origin_ HTTP** ao solicitar um recurso que tenha uma origem diferente (domínio, protocolo e porta) da sua própria origem.

O mecânismo CORS suporta requisições seguras do tipo _cross-origin e_ transferências de dados entre navegadores e servidores web. Navegadores modernos usam o CORS em uma API contêiner, como `XMLHttpRequest` ou [Fetch](https://developer.mozilla.org/pt-BR/docs/Web/API/Fetch_API), para ajudar a reduzir os riscos de requisições _cross-origin_ HTTP.

### Flask-CORS

```
pip install flask-cors
```

Essa biblioteca expõe uma aplicação Flask que, por padrão, ativa o suporte ao CORS em todas as rotas, para todas as origens e métodos. Ele permite a parametrização de todos os cabeçalhos CORS em um nível por recurso. O pacote também contém um decorator, para aqueles que preferem essa abordagem.

```python
from flask import Flask
from flask_restful import Resource, Api
from flask_jwt_extended import (
    JWTManager, jwt_required
)
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app) # Adiciona em todas as rotas
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
api = Api(app)
jwt = JWTManager(app)

class HelloWorld(Resource):
    @jwt_required
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

# OU ADICIONA POR DECORATORS

class HelloWorld(Resource):
    @jwt_required
    @cross_origin()
    def get(self):
        return {'hello': 'world'}
```
