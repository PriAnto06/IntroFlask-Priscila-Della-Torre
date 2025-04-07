from flask import Flask

app = Flask(__name__)


@app.route('/saludar/hola')
def hello():
    return 'Hello, World!'

@app.route('/saludar/chau')
def chau():
    return 'Bye'

@app.route('/sumar/<int:n1>/<int:n2>')
def sum(n1,n2):
    s = n1+n2
    return f'<p>  {n1}+{n2}={s} </p>'