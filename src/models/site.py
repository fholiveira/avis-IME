from pony.orm import Required, Set, db_session
from datetime import datetime
from .database import db


class Site(db.Entity):
    course_code = Required(str)
    teacher = Required(str)
    course = Required(str)
    hash = Required(str)
    url = Required(str)

    changed_on = Required(datetime, default=datetime.now())
    expires_on = Required(datetime)

    subscribers = Set('User')

    @db_session
    def update(self, hash):
        self.hash = hash
        self.changed_on = datetime.now()

    def to_pretty_dict(self):
        site_data = self.to_dict()
        site_data['subscribers'] = [s.email for s in self.subscribers]

        return site_data
