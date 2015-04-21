from pony.orm import Required, Set
from .database import db


class Site(db.Entity):
    course_code = Required(str)
    teacher = Required(str)
    course = Required(str)
    hash = Required(str)
    url = Required(str)

    subscribers = Set('User')
