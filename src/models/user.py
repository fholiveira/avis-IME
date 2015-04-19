from pony.orm import Required, Set
from .database import db


class User(db.Entity):
    password = Required(str)
    email = Required(str)

    feed = Set('Site')

    def get_id(self):
        return self.email

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True
