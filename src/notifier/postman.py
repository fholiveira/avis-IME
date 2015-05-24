from email.mime.multipart import MIMEMultipart
from pony.orm import select, db_session
from .comparator import SiteComparator
from email.mime.text import MIMEText
from .message import Message
from models import Site
import smtplib


class Postman:
    def __init__(self, config):
        self.config = config

    @db_session
    def _get_hashes(self):
        return select((s.id, s.url, s.hash) for s in Site)[:]

    def _get_changed_sites(self):
        sites = self._get_hashes()

        comparator = SiteComparator()

        for id, url, old_hash in sites:
            if comparator.url_and_hash(url, old_hash):
                yield (id, comparator.get_hash(url))

    @db_session
    def update_and_get_site(self, id, hash):
        site = Site[id]
        site.update(hash)

        return site.to_pretty_dict()

    def get_pending_messages(self):
        changed_sites = list(self._get_changed_sites())

        for id, hash in changed_sites:
            site = self.update_and_get_site(id, hash)

            if site['subscribers']:
                yield Message(site)

    def send(self, message):
        email = MIMEMultipart('alternative')
        email['Subject'] = message.subject()
        email['From'] = self.config.MAIL_SENDER

        email.attach(MIMEText(message.text_body(), 'plain'))
        email.attach(MIMEText(message.body(), 'html'))

        with smtplib.SMTP(self.config.MAIL_SERVER, self.config.MAIL_PORT) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(self.config.MAIL_SENDER, self.config.MAIL_PASSWD)
            server.sendmail(self.config.MAIL_SENDER, 
                            message.recipients(), 
                            email.as_string())
