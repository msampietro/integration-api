from application_properties import *
import xmlrpc.client
import logging

LOG = logging.getLogger(__name__)


def odoo_connect(db):
    try:
        if db is not None and db and isinstance(db, str):
            odoo = xmlrpc.client.ServerProxy(XMLRPC_OBJECT.format(ODOO_SERVER))
            uid = odoo.authenticate(db, ADMIN_USER, ADMIN_PASS, {})
            return uid
    except Exception as e:
        LOG.error('Error al intentar establecer conexion con Odoo: ' + str(e))
        LOG.error('Database: ' + str(db))
        LOG.error('Credentials: ' + str(ADMIN_USER) + ' - ' + str(ADMIN_PASS))
        LOG.error('Odoo Server: ' + str(ODOO_SERVER))
        LOG.error('XML OBJECT: ' + str(XMLRPC_OBJECT))

def odoo_insert(db, lead, page_name):
    try:
        uid = odoo_connect(page_name)
        if uid is not None and uid:
            models = xmlrpc.client.ServerProxy(XMLRPC_OBJECT.format(ODOO_SERVER))
            id = models.execute_kw(db, ADMIN_USER, ADMIN_PASS, ODOO_TABLE, OPERATION_CREATE, [lead])
            return 'Lead inserted with id' + id
    except Exception as e:
        print('error trying to insert the lead into odoo' + str(e))

