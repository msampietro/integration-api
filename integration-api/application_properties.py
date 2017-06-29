import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SQLITE_PATH = BASE_DIR + '\clients.db'
ODOO_SERVER = 'http://198.199.72.215:8069'
ADMIN_USER = 'tinchosampietro@hotmail.com'
ADMIN_PASS =  'odoo11223344'
DATABASE_REGEX = '(?:[0-9]{3}[A-Z]{3})'
EMAIL_REGEX = '(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'
URL_REGEX = '#/\b(([\w-]+://?|www[.])[^\s()<>]+(?:\([\w\d]+\)|([^[:punct:]\s]|/)))#iS'
CLIENTS_TABLE = 'configurations'
XMLRPC_OBJECT = '{}/xmlrpc/2/object'

'''---CONSTANTS---'''

EMPRESA_KEY = 'empresa'
DB_KEY = 'db'
USUARIO_LEAD_KEY = 'usuario_lead'


