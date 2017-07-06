import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = BASE_DIR + '\integration-api.log'
SQLITE_PATH = BASE_DIR + '\clients.db'
MAPPINGS_FILE = BASE_DIR + '\odoo_mappings.json'
ODOO_SERVER = 'http://198.199.80.95:8069'
ODOO_PORT = 8069
ADMIN_USER = 'luciano@madketing.com.ar'
ADMIN_PASS =  '123456'
DATABASE_REGEX = '(?:[0-9]{3}[A-Z]{3})'
EMAIL_REGEX = '(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'
URL_REGEX = '#/\b(([\w-]+://?|www[.])[^\s()<>]+(?:\([\w\d]+\)|([^[:punct:]\s]|/)))#iS'
CLIENTS_TABLE = 'configurations'
XMLRPC_COMMON = '{}/xmlrpc/2/common'
XMLRPC_OBJECT = '{}/xmlrpc/2/object'
XMLRPC_PROTOCOL = 'xmlrpc'
SECRET_KEY = '$0627=j55we6m#lqj5zmiryt3jmnt(#nua5*o&f6-l)dt#u&ro'
API_KEY = 'mg^-+njf=cv==l5(%&5+7o5fq6j6grc_zj!ehu$2^z(5mld)xl'
OPERATION_CREATE = 'create'
ODOO_TABLE = 'crm.lead'


'''---CONSTANTS---'''

PAGE_NAME = 'page_name'
USER_ID = 'user_id'
TYPE = 'type'
TYPE_VALUE = 'opportunity'
EMPRESA_KEY = 'empresa'
DB_KEY = 'db'
USUARIO_LEAD_KEY = 'usuario_lead'
AUTHORIZATION = 'Authorization'


