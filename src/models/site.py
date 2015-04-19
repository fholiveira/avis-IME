from pony.orm import Required, Set
from .database import db


class Site(db.Entity):
    teacher = Required(str)
    course = Required(str)
    hash = Required(str)
    url = Required(str)

    subscribers = Set('User')
