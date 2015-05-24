from flask_wtf import Form
from wtforms import StringField, TextField, PasswordField, DateField
from wtforms.validators import Required, Email, EqualTo, ValidationError, URL
from models import GateKeeper


class RegistrationForm(Form):
    email = TextField('Email', [Email(message='Email inválido.')])
    password = PasswordField('Senha', [Required(), EqualTo('confirm', message='As senhas devem ser iguais.')])
    confirm = PasswordField('Repita a senha', [Required(), EqualTo('password', message='As senhas devem ser iguais.')])

    def validate_email(form, email):
        if GateKeeper().is_registered(email.data):
            raise ValidationError('Este email já foi cadastrado.')


class LoginForm(Form):
    email = TextField('Email', [Email(message='Email inválido.')])
    password = PasswordField('Senha', [Required()])


class CourseForm(Form):
    name = TextField('Nome da matéria', [Required()])
    url = TextField('Endereço do site', [Required(), URL(message='Endereço inválido. Navegue até o site e copie o endereço mostrado no navegador.')])
    teacher = TextField('Professor', [Required()])
    code = TextField('Código', [Required()])

#    expires_on = TextField('* Parar de monitorar em', [Required()])
