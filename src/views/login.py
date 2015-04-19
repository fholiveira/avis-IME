from flask import Blueprint, render_template, request
from flask.ext.login import login_required, logout_user, login_user
from pony.orm import db_session, get
from hashlib import sha224
from models import User


access = Blueprint('auth', __name__)


@access.route('/login', methods=['POST'])
@db_session
def login():
    email = request.form['email']
    passwd = request.form['password'] 

    hash = sha224(passwd.encode('UTF-8')).hexdigest()
    
    user = get(user for user in User if user.email == email and user.password == hash)
    print(hash, user)
    login_user(user)

    return 'Bem vindo ' + user.email

@access.route('/register', methods=['POST'])
@db_session
def register():
    email = request.form['email']
    passwd = request.form['password'] 
    passwd_confirm = request.form['password_confirm']

    if passwd != passwd_confirm:
        return 'As senhas não batem!'

    hash = sha224(passwd.encode('UTF-8')).hexdigest()
    user = User(email=email, password=str(hash))
    

    return "Foi!"

@access.route("/logout")
@login_required
def logout():
    logout_user()
