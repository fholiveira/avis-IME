from flask import Blueprint, render_template, request
from flask.ext.login import current_user, login_required
from .forms import RegistrationForm, LoginForm
from pony.orm import db_session, select
from models import Site, User


home = Blueprint('home', __name__)


@home.route('/', methods=['GET'])
@db_session
def index():
    if current_user.is_authenticated():
        feed = [s.id for s in current_user.feed]
        sites= [(site.id in feed, site) 
                for site in select(s for s in Site)]

        return render_template('feed.html', sites=sites)

    return render_template('home.html',
                           login=LoginForm(), 
                           registration=RegistrationForm())


@home.route('/feed', methods=['POST'])
@db_session
@login_required
def add():
    site_id = int(request.form['id']) 
    site = Site.get(id=site_id)
    current_user.feed.add(site)
    return '', 200


@home.route('/feed', methods=['DELETE'])
@db_session
@login_required
def remove():
    site_id = int(request.form['id']) 
    site = next(s for s in current_user.feed if s.id == site_id)
    current_user.feed.remove(site)
    return '', 200
