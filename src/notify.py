#!/usr/bin/env python
from notifier import Postman
from config import load_config
from models import db


def setup_database(config):
    from models import db

    if isinstance(config.DB_DATA, str):
        db.bind(config.DB_PROVIDER, config.DB_DATA)
    else:
        db.bind(config.DB_PROVIDER, **config.DB_DATA)

    db.generate_mapping(check_tables=True, create_tables=True)


if __name__ == '__main__':
    config = load_config()
    setup_database(config)

    postman = Postman(config)
    for message in postman.get_pending_messages():
        postman.send(message)
    
