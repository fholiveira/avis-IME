from flask.ext.login import LoginManager
from pony.orm import db_session, get
from models import User

login_manager = LoginManager()

@login_manager.user_loader
@db_session
def load_user(email):
    return get(user for user in User if user.email == email)
