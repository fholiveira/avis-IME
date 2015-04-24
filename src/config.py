from urllib.parse import urlparse
from os import getenv


class DevelopmentConfig:
    SERVER_NAME = 'localhost:5000'
    MAIL_PASSWD = '111111111111'
    MAIL_SENDER = 'aaa@bbb.com'
    MAIL_SERVER = 'smpt.dev.com'
    MAIL_PORT = 123
    SECRET_KEY = 'secret_key'
    ENVIRONMENT_NAME = 'DEV'
    DB_PROVIDER = 'sqlite'
    DB_DATA = 'avis-ime.db'
    TESTING = False
    DEBUG = True


class TestConfig:
    SERVER_NAME = 'localhost:5005'
    MAIL_PASSWD = '111111111111'
    MAIL_SENDER = 'aaa@bbb.com'
    MAIL_SERVER = 'smpt.dev.com'
    MAIL_PORT = 123
    SECRET_KEY = 'secret_key'
    ENVIRONMENT_NAME = 'TEST'
    DB_PROVIDER = 'sqlite'
    DB_DATA = 'avis-ime-test.db'
    TESTING = True
    DEBUG = False


class DeployConfig:
    ENVIRONMENT_NAME = 'DEPLOY'
    DB_PROVIDER = 'mysql'
    TESTING = False
    DEBUG = False

    def __init__(self):
        self.MAIL_SENDER = getenv('AVISIME_MAIL_SENDER')
        self.MAIL_PASSWD = getenv('AVISIME_MAIL_PASSWD')
        self.MAIL_SERVER = getenv('AVISIME_MAIL_SERVER')
        self.MAIL_PORT = int(getenv('AVISIME_MAIL_PORT', default=0))
        self.SECRET_KEY = getenv('AVISIME_SECRET_KEY')
        self.DB_DATA = {'user':  getenv('AVISIME_DB_USERNAME'),
                        'passwd': getenv('AVISIME_DB_PASSWORD'),
                        'host': getenv('AVISIME_DB_HOST'),
                        'db': getenv('AVISIME_DB_NAME')}


def load_config():
    env = getenv('AVISIME_ENV', 'DEPLOY')

    configs = {DevelopmentConfig.ENVIRONMENT_NAME: DevelopmentConfig,
               DeployConfig.ENVIRONMENT_NAME: DeployConfig,
               TestConfig.ENVIRONMENT_NAME: TestConfig}

    return configs[env.upper()]()
