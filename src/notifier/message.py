from pony.orm import db_session
from config import load_config
from models import Site, User


class Message:
    def __init__(self, site):
        self.site = site

    def recipients(self):
        return [email for email in self.site['subscribers']]

    def body(self):
        return """\
            <html>
                <head></head>
                <body>
                    <p>Olá!<br>
                        <br>
                        O professor de {course} atualizou seu site. Clique <a href="{url}">aqui</a> para conferir as mudanças.
                    </p>
                </body>
            </html>
        """.format(**self.site)

    def text_body(self):
        return "Olá! O professor de {course} atualizou seu site. Clique <a href=\"{url}\">aqui</a> para conferir as mudanças.".format(**self.site)

    def subject(self):
        return "O professor de {course} atualizou o seu site".format(**self.site)
