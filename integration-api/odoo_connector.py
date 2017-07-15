from application_properties import *
import xmlrpc.client
import logging
LOG = logging.getLogger(__name__)


def odoo_connect(db):
    try:
        if db is not None and db and isinstance(db, str):
            odoo = xmlrpc.client.ServerProxy(XMLRPC_COMMON.format(ODOO_SERVER))
            uid = odoo.authenticate(db, ADMIN_USER, ADMIN_PASS, {})
            return uid
    except Exception as e:
        LOG.error('Error al intentar establecer conexion con Odoo: ' + str(e))
        LOG.error('Database: ' + str(db))
        LOG.error('Credentials: ' + str(ADMIN_USER) + ' - ' + str(ADMIN_PASS))
        LOG.error('Odoo Server: ' + str(ODOO_SERVER))
        LOG.error('XML OBJECT: ' + str(XMLRPC_OBJECT))

def odoo_insert(db, lead):
    try:
        uid = odoo_connect(db)
        if uid is not False and isinstance(uid, int):
            models = xmlrpc.client.ServerProxy(XMLRPC_OBJECT.format(ODOO_SERVER))
            id = models.execute_kw(db, uid, ADMIN_PASS, ODOO_TABLE, OPERATION_CREATE, [lead])
            return 'Lead insertado con id' + str(id)
        else:
            LOG.error('El usuario no pudo ser autenticado')
    except Exception as e:
        LOG.error('Error al intentar insertar Lead en Odoo' + str(e))

def get_user_id(db, user_email, uid):
    try:
        if uid is not None and uid:
            models = xmlrpc.client.ServerProxy(XMLRPC_OBJECT.format(ODOO_SERVER))
            ids = models.execute_kw(db, uid, ADMIN_PASS, 'res.users', 'search', [[['login', '=', user_email]]])
            return ids[0]
    except Exception as e:
        LOG.error('No pudo leerse el usuario de la base de datos de Odoo' + str(e))