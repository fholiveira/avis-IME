from flask.ext.login import LoginManager
from pony.orm import db_session, get
from models import User

login_manager = LoginManager()

@login_manager.user_loader
def load_user(email):
    user = None 

    with db_session:
        user = get(user for user in User if user.email == email)

    return user
