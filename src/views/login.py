from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask.ext.login import login_required, logout_user, login_user
from .forms import RegistrationForm, LoginForm
from models import GateKeeper


access = Blueprint('login', __name__)


@access.route('/login', methods=['POST'])
def login():
    form = LoginForm()
    try_again = render_template('home.html',
                                login=form, 
                                registration=RegistrationForm())

    if not form.validate():
        return try_again

    user = GateKeeper().grant_access(form.email.data, form.password.data)

    if not user:
        flash('Usuário ou senha inválidos.')
        return try_again

    login_user(user)

    return redirect(url_for('home.index'))

@access.route('/register', methods=['POST'])
def register():
    form = RegistrationForm()
    if not form.validate():
        return render_template('home.html',
                               login=LoginForm(), 
                               registration=form)

    user = GateKeeper().register(form.email.data, form.password.data)
    login_user(user)

    return redirect(url_for('home.index'))

@access.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home.index'))
