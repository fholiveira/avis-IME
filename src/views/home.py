from flask import Blueprint, render_template, request
from flask.ext.login import current_user, login_required
from .forms import RegistrationForm, LoginForm
from models import Feed


home = Blueprint('home', __name__)


@home.route('/', methods=['GET'])
def index():
    if current_user.is_authenticated():
        return render_template('feed.html', sites=Feed(current_user.id).sites())

    return render_template('home.html',
                           login=LoginForm(), 
                           registration=RegistrationForm())


@home.route('/feed', methods=['POST'])
@login_required
def add():
    site = int(request.form['id']) 
    Feed(current_user.id).add(site)

    return '', 200


@home.route('/feed', methods=['DELETE'])
@login_required
def remove():
    site = int(request.form['id']) 
    Feed(current_user.id).remove(site)

    return '', 200
