from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from flask import render_template, session, flash, redirect, url_for

from . import auth
from app.forms import LoginForm, SignUpForm
from app.firestore_service import get_user, put_user, put_init_todo
from app.models import UserModel, UserData, DefaultTodo

@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    context = {
        'login_form': login_form
    }

    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data

        user_doc = get_user(username)

        if user_doc.to_dict() is not None:
            password_from_db = user_doc.to_dict()['password']

            if check_password_hash(password_from_db, password):
                user_data = UserData(username, password)
                user = UserModel(user_data)
                login_user(user)

                flash('Bienvenido de nuevo')

                redirect(url_for('welcome'))
            else:
                flash('La información no coincide')
        else:
            flash('El usario no existe')

        return redirect(url_for('home'))

    return render_template('login.html', **context)


@auth.route("/signup", methods=['GET', 'POST'])
def signup():
    signup_form = SignUpForm()
    context = {
        'signup_form':signup_form,
    }

    if signup_form.validate_on_submit():
        username = signup_form.username.data
        password = signup_form.password.data
        re_password = signup_form.re_password.data
 
        if password == re_password:
            user_doc = get_user(username)
            if user_doc.to_dict() is None:
                hash_password =  generate_password_hash(password)
                user_data = UserData(username, hash_password)
                put_user(user_data)

                put_init_todo(DefaultTodo(username))

                user = UserModel(user_data)
                login_user(user)

                flash("Bienvenido")
                return redirect(url_for('welcome'))

            else:
                flash("usuario existe.")      
        
        else:
            flash("Contraseñas no coinciden.")


    return render_template("signup.html", **context)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Ten un buen día!")
    return redirect(url_for("home"))

