from flask import render_template, session, flash, redirect, url_for
from app.forms import LoginForm, SignUpForm
from . import auth
from app.firestore_service import get_user
from app.models import UserModel, UserData
from flask_login import login_user, logout_user

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

            print(user_doc.to_dict())
            print(user_doc.to_dict()['password'])

            if password == password_from_db:
                user_data = UserData(username, password)
                user = UserModel(user_data)
                login_user(user)

                flash('Bienvenido de nuevo')

                redirect(url_for('welcome'))
            else:
                flash('La informaición no coincide')
        else:
            flash('El usario no existe')

        return redirect(url_for('home'))

    return render_template('login.html', **context)

@auth.route("/logout")
def logout():
    logout_user()
    flash("Ten un buen día!")
    return redirect(url_for("home"))

@auth.route("/signup")
def signup():
    signup_form = SignUpForm()
    context = {
        'signup_form':signup_form,
    }

    return render_template("signup.html", **context)
