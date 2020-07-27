from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)           # Crea instancia de Flask, cuyo parametro __name__ (nombre del archivo) será el nombre de la app.

todos = ['Todo 1', 'Todo 2', 'Todo 3', 'Todo 4']

@app.route('/') # Ruta donde se correrá esta función. Es decir, Cuando el buscador haga una petición a nuestro servidor, va a llegar a ruta raiz.
def index():
    user_ip = request.remote_addr   #obtiene la ip de la conexión remota
    make_redir = redirect("/hello")
    response = make_response(make_redir)
    response.set_cookie('user_ip', user_ip)

    return response


@app.route('/hello')    
def hello():
    user_ip = request.cookies.get('user_ip')
    context = {
        'user_ip':user_ip, 
        'todos':todos,
    }
    
    return render_template('hello.html', **context)     # expande el diccionario para pasar cada una de las variables
   




# \venv\Scripts\activate
# set FLASK_APP=main.py     -> establece la variable FLASK_APP a main.py
# set FLASK_DEBUG=1         -> establece la variable FLASK_DEBUGG a 1 para habilitar debug mode
# flas run

# Estructuras de control
# 1.- detectar ip
# 2.- si, regresamos mensaje
# 3.- si no, crear link que vuelva  a raiz y asi obtener ip y devolvernos a hello
#
#
# 2.- Crear una variable de lista e iterar en cada string.
