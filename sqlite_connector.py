import sqlite3
from application_properties import *
from utils import validate_regex, build_response
import logging
from clients_form import ClientForm, ClientList

LOG = logging.getLogger(__name__)

def sqlite_connect():
    try:
        conn = sqlite3.connect(SQLITE_PATH)
        c = conn.cursor()
        return c, conn
    except sqlite3.Error as sqe:
        LOG.error('Sqlite Error durante la conexion: ' + str(sqe))
        LOG.error('Database path: ' + SQLITE_PATH)


def new_client(company, db, user_lead):
    c, conn = sqlite_connect()
    try:
        if c and conn:
            if isinstance(company, str) and validate_regex(db, DATABASE_REGEX) \
                    and validate_regex(user_lead, EMAIL_REGEX):
                client = (company, db, user_lead)
                insert_query = 'INSERT INTO ' + CLIENTS_TABLE + ' VALUES (NULL, ?, ?, ?)'
                c.execute(insert_query, client)
                conn.commit()
                message = build_response('Cliente almacenado con exito!', 200)
            else:
                message = build_response('Error en los datos, verificar formato de MAIL y BASE DE DATOS', 400)
    except sqlite3.Error as sqe:
        message = build_response('Error al intentar almacenar el cliente, es posible que alguno de los datos especificados ya exista', 400)
        LOG.error('Sqlite Error al insertar ' + str(sqe))
        LOG.error('Parametros recibidos: ' + str(client))
        LOG.error('Query: ' + str(insert_query))

    finally:
        conn.close()

    return message

def get_database(client_name):
    c, conn = sqlite_connect()
    data = None
    if client_name and isinstance(client_name, str):
        try:
            select_query = "SELECT "+ DB_KEY +" FROM " + CLIENTS_TABLE + " WHERE " + EMPRESA_KEY + " = '%s'"
            c.execute(select_query % client_name)
            data = c.fetchone()
            if data is not None and data and isinstance(data, tuple):
                data = data[0]
        except sqlite3.Error as sqe:
            LOG.error('Sqlite Error al intentar recuperar registros de la db: ' + str(sqe))
            LOG.error('Query: ' + str(select_query))
            LOG.error('Client name: ' + str(client_name))

        finally:
            conn.close()

    return data

def get_user(client_name):
    c, conn = sqlite_connect()
    data = None
    if client_name and isinstance(client_name, str):
        try:
            select_query = "SELECT "+ USUARIO_LEAD_KEY +" FROM " + CLIENTS_TABLE + " WHERE " + EMPRESA_KEY + " = '%s'"
            c.execute(select_query % client_name)
            data = c.fetchone()
            if data is not None and data and isinstance(data, tuple):
                data = data[0]
        except sqlite3.Error as sqe:
            LOG.error('Sqlite Error al intentar recuperar registros de la db: ' + str(sqe))
            LOG.error('Query: ' + str(select_query))
            LOG.error('Client name: ' + str(client_name))

        finally:
            conn.close()

    return data

def list_clients():
    c,conn = sqlite_connect()
    clients = ClientList()
    try:
        select_query = "SELECT * FROM " + CLIENTS_TABLE
        c.execute(select_query)
        data = c.fetchall()
        if data is not None and data and (isinstance(data, list) or isinstance(data, tuple)):
            for d in data:
                client = ClientForm()
                client.empresa = d[1]
                client.db = d[2]
                client.usuario_lead = d[3]
                clients.client_list.append_entry(client)
    except sqlite3.Error as sqe:
        LOG.error('Sqlite Error al intentar recuperar registros de la db: ' + str(sqe))
        LOG.error('Query: ' + str(select_query))

    finally:
        conn.close()

    return clients
