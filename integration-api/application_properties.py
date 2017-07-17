'''Application Properties and Configurations'''

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if os.name == 'nt':
    LOG_FILE = BASE_DIR + '\integration-api.log'
    SQLITE_PATH = BASE_DIR + '\docker-volume\clients.db'
    MAPPINGS_FILE = BASE_DIR + '\odoo_mappings.json'
    COMPOUND_FILE = BASE_DIR + '\json_compound.json'
else:
    LOG_FILE = BASE_DIR + '/integration-api.log'
    SQLITE_PATH = BASE_DIR + '/docker-volume/clients.db'
    MAPPINGS_FILE = BASE_DIR + '/odoo_mappings.json'
    COMPOUND_FILE = BASE_DIR + '/json_compound.json'
ODOO_SERVER = 'https://crm.madketing.com.ar'
ODOO_PORT = 8069
ADMIN_USER = 'crm@madketing.com.ar'
ADMIN_PASS =  'madketing1189'
DATABASE_REGEX = '(?:[0-9]{3}[A-Z]{3})'
EMAIL_REGEX = '(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'
URL_REGEX = '#/\b(([\w-]+://?|www[.])[^\s()<>]+(?:\([\w\d]+\)|([^[:punct:]\s]|/)))#iS'
PAGE_NAME_REGEX = "(?![0-9])([[a-zA0-z9]+)"
CLIENTS_TABLE = 'configurations'
USERS_TABLE = 'users'
XMLRPC_COMMON = '{}/xmlrpc/2/common'
XMLRPC_OBJECT = '{}/xmlrpc/2/object'
XMLRPC_PROTOCOL = 'xmlrpc'
SECRET_KEY = '$0627=j55we6m#lqj5zmiryt3jmnt(#nua5*o&f6-l)dt#u&ro'
API_KEY = 'mg^-+njf=cv==l5(%&5+7o5fq6j6grc_zj!ehu$2^z(5mld)xl'
OPERATION_CREATE = 'create'
ODOO_TABLE = 'crm.lead'
APPEND_FIELD = 'description'
APPEND_SEPARATOR = ' - '