#!/usr/bin/env python
def setup_database(config):
    from models import db

    if isinstance(config.DB_DATA, str):
        db.bind(config.DB_PROVIDER, config.DB_DATA)
    else:
        db.bind(config.DB_PROVIDER, **config.DB_DATA)


from config import load_config
from flask import Flask
from views import home


config = load_config()
setup_database(config)

webapp = Flask(__name__)
webapp.config.from_object(config)
webapp.register_blueprint(home)


if __name__ == '__main__':
    from wando import ColoredLogsRequestHandler

    print('Using', webapp.config['ENVIRONMENT_NAME'], 'environment.' )
    webapp.run(request_handler=ColoredLogsRequestHandler)
