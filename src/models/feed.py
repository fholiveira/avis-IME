from pony.orm import db_session, select
from models import Site, User


class Feed:
    def __init__(self, user_id):
        self.user_id = user_id

    @db_session
    def add(self, site):
        User[self.user_id].feed.add(Site[site])
        
    @db_session
    def remove(self, site):
        User[self.user_id].feed.remove(Site[site])

    @db_session
    def sites(self):
        feed = [f.id for f in User[self.user_id].feed]
        sites = select(s for s in Site)

        return [(site.id in feed, site) for site in sites]
