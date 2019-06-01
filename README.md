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