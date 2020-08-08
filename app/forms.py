from wtforms import PasswordField, SubmitField, StringField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

class LoginForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Ingresar')

class SignUpForm(FlaskForm):
    username    = StringField("Usuario", validators=[DataRequired()])
    password    = PasswordField("Contraseña", [DataRequired()])
    re_password = PasswordField("Repetir Contraseña", [DataRequired()])
    submit      = SubmitField("Registrar")

class TodoForm(FlaskForm):
    description = StringField("",  validators=[DataRequired()], render_kw={"placeholder": "Nuevo recordatorio."})
    submit = SubmitField("Agregar")

class DeleteForm(FlaskForm):
    submit = SubmitField("Borrar")

class UpdateForm(FlaskForm):
    submit = SubmitField("Actualizar")