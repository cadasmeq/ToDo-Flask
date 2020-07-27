from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)           # Crea instancia de Flask, cuyo parametro __name__ (nombre del archivo) será el nombre de la app.

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
    
    return render_template('hello.html', user_ip=user_ip)
   

# \venv\Scripts\activate
# set FLASK_APP=main.py     -> establece la variable FLASK_APP a main.py
# set FLASK_DEBUG=1         -> establece la variable FLASK_DEBUGG a 1 para habilitar debug mode
# flas run

# Renderear templates
