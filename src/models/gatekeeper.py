from pony.orm import db_session, get, count
from hashlib import sha224
from models import User


class GateKeeper:
    @db_session
    def identify(self, email):
        return get(user for user in User if user.email == email)

    @db_session
    def grant_access(self, email, passwd):
        passwd_hash = sha224(passwd.encode('UTF-8')).hexdigest()
        return User.get(email = email, password = str(passwd_hash))

    @db_session
    def register(self, email, passwd):
        if self.is_registered(email):
            raise Exception('Email já cadastrado!')

        passwd_hash = sha224(passwd.encode('UTF-8')).hexdigest()
        return User(email=email, password=str(passwd_hash))

    @db_session
    def is_registered(self, email):
        return count(user for user in User if user.email == email) > 0
