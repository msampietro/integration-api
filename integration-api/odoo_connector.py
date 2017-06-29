from application_properties import *
import xmlrpc.client

def odoo_connect(db):
    try:
        if db is not None and db and isinstance(db,str):
            odoo = xmlrpc.client.ServerProxy(XMLRPC_OBJECT.format(ODOO_SERVER))
            uid = odoo.authenticate(db[0], ADMIN_USER, ADMIN_PASS, {})
            return uid
    except Exception as e:
        print('error trying to establish odoo connection: ' + str(e))
