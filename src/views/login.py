from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask.ext.login import login_required, logout_user, login_user
from .forms import RegistrationForm, LoginForm
from models import GateKeeper


access = Blueprint('login', __name__)


def try_again(form):
    load_form = lambda tipo: form if isinstance(form, tipo) else tipo()

    return render_template('home.html',
                           login = load_form(LoginForm), 
                           registration = load_form(RegistrationForm))


@access.route('/login', methods=['GET'])
@access.route('/register', methods=['GET'])
def go_to_home():
    return redirect(url_for('home.index'))


@access.route('/login', methods=['POST'])
def login():
    form = LoginForm()

    if not form.validate():
        return try_again(form)

    user = GateKeeper().grant_access(form.email.data, form.password.data)

    if not user:
        flash('Usuário ou senha inválidos.')
        return try_again(form)

    login_user(user)

    return go_to_home()


@access.route('/register', methods=['POST'])
def register():
    form = RegistrationForm()
    if not form.validate():
        return try_again(form)

    user = GateKeeper().register(form.email.data, form.password.data)
    login_user(user)

    return go_to_home()


@access.route("/logout")
@login_required
def logout():
    logout_user()
    return go_to_home()
