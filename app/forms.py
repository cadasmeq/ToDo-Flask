from wtforms import PasswordField, SubmitField, StringField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class SignUpForm(FlaskForm):
    username    = StringField("Username", validators=[DataRequired()])
    password    = PasswordField("Password", [DataRequired()])
    re_password = PasswordField("Repeat Password", [DataRequired()])
    submit      = SubmitField("Sign Up")  