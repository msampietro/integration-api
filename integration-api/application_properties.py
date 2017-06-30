import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = BASE_DIR + '\integration-api.log'
SQLITE_PATH = BASE_DIR + '\clients.db'
ODOO_SERVER = 'http://198.199.72.215:8069'
ADMIN_USER = 'tinchosampietro@hotmail.com'
ADMIN_PASS =  'odoo11223344'
DATABASE_REGEX = '(?:[0-9]{3}[A-Z]{3})'
EMAIL_REGEX = '(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'
URL_REGEX = '#/\b(([\w-]+://?|www[.])[^\s()<>]+(?:\([\w\d]+\)|([^[:punct:]\s]|/)))#iS'
CLIENTS_TABLE = 'configurations'
XMLRPC_OBJECT = '{}/xmlrpc/2/object'
SECRET_KEY = '$0627=j55we6m#lqj5zmiryt3jmnt(#nua5*o&f6-l)dt#u&ro'
OPERATION_CREATE = 'create'
ODOO_TABLE = 'crm.lead'


'''---CONSTANTS---'''
PAGE_NAME = 'page_name'
EMPRESA_KEY = 'empresa'
DB_KEY = 'db'
USUARIO_LEAD_KEY = 'usuario_lead'


