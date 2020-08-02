from flask import Flask, request, redirect, make_response, render_template, session
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
check = True
todos = ["Limpiar la mesa", "Hacer ejercicio", "Leer un libro"]
app.config['SECRET_KEY'] = "THIS_IS_THE_KEY"
params = {}

@app.route("/") #home?
def home():
    remote_ip = request.remote_addr
    make_redir  = redirect("/myIP")
    response = make_response(make_redir)
    session['ip_user'] = remote_ip
    # response.set_cookie("ip_user", remote_ip)

    return response
    

@app.route('/myIP')
def myIP():
    #ip_user = request.cookies.get('ip_user')
    ip_user = session.get('ip_user')
    params = {
        "ip_user":ip_user,
        "todos":todos,
        'check':check
    }
    
    return render_template('myip.html', **params)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error=error)


# NOTAS
# Se declará el nombre de la app
# Utilizando request, se le pide la IP al cliente web.
# Con make_response, se generá una respuesta a cliente que lo redireccióna al path indicado.
# Se le genera una cookie al cliente que almacena su dirección IP.
# Tras la redirección se obtiene la info de la cookie y se imprime en pantalla.
# Se agrega render_template (path por defecto ./template).
# Para agregar código de python en los archivos html se utilizan las estructuras de control.
# en myip.html, se agregan dos estructuras de control, condicional (if) y ciclica (for) 
# Se agregan a diccionario algunos parametros del render_template y al usar **params, se expande diccionarió completo.

# Se agrega check al diccionario.