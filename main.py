import unittest
from flask import Flask, request, redirect, make_response, render_template, session, url_for, flash
from flask_login import login_required, current_user

from app import create_app
from app.forms import LoginForm
from app.firestore_service import get_users, get_todos


app = create_app()

params = {}

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('test')
    unittest.TextTestRunner().run(tests)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error=error)

@app.route("/")
def home():
    remote_ip = request.remote_addr
    response = make_response(redirect("welcome"))
    session['ip_user'] = remote_ip

    return response

@app.route('/welcome')
@login_required
def welcome():
    ip_user = session.get('ip_user')
    username = current_user.id

    params = {
        "ip_user":ip_user,
        "todos": get_todos(username),
        'username':username,
    }

    return render_template('welcome.html', **params)