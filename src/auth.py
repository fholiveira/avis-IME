from flask.ext.login import LoginManager
from models import GateKeeper


login_manager = LoginManager()


@login_manager.user_loader
def load_user(email):
    return GateKeeper().identify(email)
