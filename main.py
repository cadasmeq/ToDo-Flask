import unittest
from flask import Flask, request, redirect, make_response, render_template, session, url_for, flash
from flask_login import login_required, current_user

from app import create_app
from app.forms import TodoForm, DeleteForm, UpdateForm
from app.firestore_service import get_users, get_todos, put_todo, delete_todo, update_todo

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

@app.route('/welcome', methods=['GET', 'POST'])
@login_required
def welcome():
    ip_user = session.get('ip_user')
    username = current_user.id
    
    todo_form = TodoForm()
    update_form = UpdateForm()
    delete_form = DeleteForm()

    params = {
        "ip_user":ip_user,
        'username':username,
        "todos": get_todos(username),
        'todo_form':todo_form,
        'update':update_form,
        'delete':delete_form,
    }
        
    if todo_form.validate_on_submit():
        put_todo(user_id=username, description=todo_form.description.data)
        flash("Todo Added.")
        return redirect(url_for("welcome"))

    return render_template('welcome.html', **params)

@app.route('/todos/delete/<todo_id>', methods=['POST'])
def delete(todo_id):
    user_id = current_user.id
    delete_todo(user_id, todo_id)

    return redirect(url_for('welcome'))

@app.route('/todos/update/<todo_id>/<int:status>', methods=['POST'])
def update(todo_id, status):
    user_id = current_user.id
    update_todo(user_id, todo_id, status)
    
    return redirect(url_for('welcome'))
