#flask配置


HOSTNAME = '127.0.0.1'
DATABASE = 'xymessageborad'
PORT = 3306
USERNAME = 'root'
PASSWORD = 'han200833'


class Config:
    template_folder = './templates'
    DB_URL = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
    static_folder = './static'



