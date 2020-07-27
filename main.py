from flask import Flask

app = Flask(__name__)           # Crea instancia de Flask, cuyo parametro __name__ (nombre del archivo) será el nombre de la app.

@app.route('/')    # Ruta donde se correrá esta función. Es decir, Cuando el buscador haga una petición a nuestro servidor, va a llegar a ruta raiz.
def hello():
    return "hello world Flask"