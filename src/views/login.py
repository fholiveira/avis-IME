from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask.ext.login import login_required, logout_user, login_user
from .forms import RegistrationForm, LoginForm
from pony.orm import db_session, get
from hashlib import sha224
from models import User


access = Blueprint('login', __name__)


@access.route('/login', methods=['POST'])
@db_session
def login():
    form = LoginForm()
    if not form.validate():
        return render_template('home.html',
                               login=form, 
                               registration=RegistrationForm())

    hash = sha224(form.password.data.encode('UTF-8')).hexdigest()
    
    user = get(user for user in User
               if user.email == form.email.data and user.password == hash)

    if not user:
        flash('Usuário ou senha inválidos.')
        return render_template('home.html',
                               login=form, 
                               registration=RegistrationForm())

    login_user(user)

    return redirect(url_for('home.index'))

@access.route('/register', methods=['POST'])
@db_session
def register():
    form = RegistrationForm()
    if not form.validate():
        return render_template('home.html',
                               login=LoginForm(), 
                               registration=form)

    hash = sha224(form.password.data.encode('UTF-8')).hexdigest()
    user = User(email=form.email.data, password=str(hash))
    
    login_user(user)

    return redirect(url_for('home.index'))

@access.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home.index'))
