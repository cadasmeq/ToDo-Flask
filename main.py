from flask import Flask, request, redirect, make_response, render_template, session, url_for, flash
from app import create_app
import unittest
from app.forms import LoginForm

app = create_app()

params = {}
check = True
todos = ["Limpiar la mesa", "Hacer ejercicio", "Leer un libro"]

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('test')
    unittest.TextTestRunner().run(tests)

@app.route("/") #home?
def home():
    remote_ip = request.remote_addr
    make_redir  = redirect("/myIP")
    response = make_response(make_redir)
    session['ip_user'] = remote_ip
    # response.set_cookie("ip_user", remote_ip)

    return response
    
@app.route('/myIP', methods=['GET', 'POST'])
def myIP():
    #ip_user = request.cookies.get('ip_user')
    login_form = LoginForm()
    ip_user = session.get('ip_user')
    username = session.get('username')

    params = {
        "ip_user":ip_user,
        'login_form':login_form,
        "todos":todos,
        'check':check,
        'username':username,
    }

    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username
        flash("Usuario registrado con exito.")

        return redirect(url_for('home'))
    
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