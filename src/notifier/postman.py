from email.mime.multipart import MIMEMultipart
from pony.orm import select, db_session
from email.mime.text import MIMEText
from .message import Message
from hashlib import sha224
from smtplib import SMTP
from requests import get
from models import Site


class Postman:
    def __init__(self, config):
        self.config = config

    @db_session
    def send_pending_mails(self):
        for site in select(s for s in Site):
            html = get(site.url)
            hash = sha224(html.text.encode('UTF-8')).hexdigest()

            if site.hash == hash:
                return

            if any(site.subscribers):
                self.send(Message(site))

            site.hash = hash

    def send(self, message):
        email = MIMEMultipart('alternative')
        email['Subject'] = message.subject()
        email['From'] = self.config.MAIL_SENDER
        email['To'] = ', '.join(message.recipients())
        print(email['To'])

        email.attach(MIMEText(message.text_body(), 'plain'))
        email.attach(MIMEText(message.body(), 'html'))

        with SMTP(self.config.MAIL_SERVER, self.config.MAIL_PORT) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(self.config.MAIL_SENDER, self.config.MAIL_PASSWD)
            server.sendmail(self.config.MAIL_SENDER, 
                            self.config.MAIL_SENDER, 
                            email.as_string())

            server.close()
