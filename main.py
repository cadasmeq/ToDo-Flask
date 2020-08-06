from flask import Flask, request, redirect, make_response, render_template, session, url_for, flash
from app import create_app
import unittest
from app.forms import LoginForm

app = create_app()

params = {}

todos = ["Implementar POST", "Hacer ejercicio", "Leer un libro"]

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('test')
    unittest.TextTestRunner().run(tests)

@app.route("/")
def home():
    remote_ip = request.remote_addr
    make_redir  = redirect("/auth/login")
    response = make_response(make_redir)
    session['ip_user'] = remote_ip

    return response
    
@app.route('/welcome')
def welcome():

    ip_user = session.get('ip_user')
    username = session.get('username')

    params = {
        "ip_user":ip_user,
        "todos":todos,
        'username':username,
    }

    return render_template('welcome.html', **params)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error=error)