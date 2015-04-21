from flask_wtf import Form
from wtforms import StringField, TextField, PasswordField
from wtforms.validators import Required, Email, EqualTo


class RegistrationForm(Form):
    email = TextField('Email', [Email(message='Email inválido.')])
    password = PasswordField('Senha', [Required(), EqualTo('confirm', message='As senhas devem ser iguais.')])
    confirm = PasswordField('Repita a senha', [Required(), EqualTo('password', message='As senhas devem ser iguais.')])

class LoginForm(Form):
    email = TextField('Email', [Email(message='Email inválido.')])
    password = PasswordField('Senha', [Required()])
