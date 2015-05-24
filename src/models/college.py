from pony.orm import db_session, get, count
from notifier import SiteComparator
from datetime import datetime
from hashlib import sha224
from models import Site


class College:
    @db_session
    def register(self, name, code, teacher, url):
        if self.contains_course(code):
            raise Exception('Este curso já está sendo monitorado!')

        comparator = SiteComparator()

        if not comparator.is_hashable(url):
            raise Exception('Este site não pode ser monitorado :(')

        site_hash = comparator.get_hash(url)

        Site(expires_on=datetime(2016, 2, 1),
             course_code=code,
             teacher=teacher,
             hash=site_hash,
             course=name,
             url=url)

    @db_session
    def contains_course(self, code):
        return count(course for course in Site if course.course_code == code) > 0
