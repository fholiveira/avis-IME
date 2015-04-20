from flask import Blueprint, render_template
from flask.ext.login import current_user


home = Blueprint('', __name__)


@home.route('/', methods=['GET'])
def index():
    if current_user.is_authenticated():
        return render_template('feed.html')

    return render_template('home.html')
