#!/usr/bin/env python
def setup_database(config):
    from models import db

    if isinstance(config.DB_DATA, str):
        db.bind(config.DB_PROVIDER, config.DB_DATA)
    else:
        db.bind(config.DB_PROVIDER, **config.DB_DATA)

    db.generate_mapping(check_tables=True, create_tables=True)


from config import load_config
from flask import Flask


config = load_config()


from views import access, home, courses
from auth import login_manager

login_manager.session_protection = config.SECRET_KEY

webapp = Flask(__name__)
login_manager.init_app(webapp)
webapp.config.from_object(config)

webapp.register_blueprint(access)
webapp.register_blueprint(home)
webapp.register_blueprint(courses)

setup_database(config)


if __name__ == '__main__':
    from wando import ColoredLogsRequestHandler

    print('Using', webapp.config['ENVIRONMENT_NAME'], 'environment.' )
    webapp.run(request_handler=ColoredLogsRequestHandler)
