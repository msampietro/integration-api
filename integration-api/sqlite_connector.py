import sqlite3
from application_properties import *
from utils import validate_regex, build_response
from application_constants import *
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


def new_client(company, db):
    c, conn = sqlite_connect()
    try:
        if c and conn:
            if isinstance(company, str) and validate_regex(db, DATABASE_REGEX):
                client = (company, db)
                insert_query = 'INSERT INTO ' + CLIENTS_TABLE + ' VALUES (NULL, ?, ?)'
                c.execute(insert_query, client)
                conn.commit()
                message = build_response('Cliente almacenado con exito!', 200)
            else:
                message = build_response('Error en los datos, verificar formato de BASE DE DATOS', 400)
    except sqlite3.Error as sqe:
        message = build_response('Error al intentar almacenar el cliente, es posible que alguno de los datos especificados ya exista', 400)
        LOG.error('Sqlite Error al insertar ' + str(sqe))
        LOG.error('Parametros recibidos: ' + str(client))
        LOG.error('Query: ' + str(insert_query))

    finally:
        conn.close()

    return message

def new_user(user, password):
    c, conn = sqlite_connect()
    try:
        if c and conn:
            client = (user, password)
            insert_query = 'INSERT INTO ' + USERS_TABLE + ' VALUES (NULL, ?, ?)'
            c.execute(insert_query, client)
            conn.commit()
            message = build_response('Usuario almacenado con exito!', 200)
    except sqlite3.Error as sqe:
        message = build_response('Error al intentar almacenar el usuario, es posible que alguno de los datos especificados ya exista', 400)
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
            select_query = "SELECT "+ DB_KEY +" FROM " + CLIENTS_TABLE + " WHERE " + EMPRESA_KEY + " LIKE '%s'"
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
            select_query = "SELECT "+ USUARIO_LEAD_KEY +" FROM " + CLIENTS_TABLE + " WHERE " + EMPRESA_KEY + " LIKE '%s'"
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
    c, conn = sqlite_connect()
    clients = ClientList()
    try:
        select_query = "SELECT * FROM " + CLIENTS_TABLE
        c.execute(select_query)
        data = c.fetchall()
        if data is not None and data and (isinstance(data, list) or isinstance(data, tuple)):
            for d in data:
                client = ClientForm()
                client.codigo = d[0]
                client.empresa = d[1]
                client.db = d[2]
                clients.client_list.append_entry(client)
    except sqlite3.Error as sqe:
        LOG.error('Sqlite Error al intentar recuperar registros de la db: ' + str(sqe))
        LOG.error('Query: ' + str(select_query))

    finally:
        conn.close()

    return clients

def list_users():
    c, conn = sqlite_connect()
    try:
        select_query = "SELECT * FROM " + USERS_TABLE
        c.execute(select_query)
        data = c.fetchall()
    except sqlite3.Error as sqe:
        LOG.error('Sqlite Error al intentar recuperar registros de la db: ' + str(sqe))
        LOG.error('Query: ' + str(select_query))

    finally:
        conn.close()

    return data

def update_client(company, db, id):
    c, conn = sqlite_connect()
    try:
        if c and conn:
            if isinstance(company, str) and validate_regex(db, DATABASE_REGEX):
                client = (company, db, id)
                update_query = 'UPDATE ' + CLIENTS_TABLE + ' SET empresa=?,db=? WHERE id=?'
                c.execute(update_query, client)
                conn.commit()
                message = build_response('Cliente actualizado con exito!', 200)
            else:
                message = build_response('Error en los datos, verificar formato de BASE DE DATOS', 400)
    except sqlite3.Error as sqe:
        message = build_response('Error al intentar actualizar el cliente, es posible que alguno de los datos especificados ya exista', 400)
        LOG.error('Sqlite Error al actualizar ' + str(sqe))
        LOG.error('Parametros recibidos: ' + str(client))
        LOG.error('Query: ' + str(update_query))

    finally:
        conn.close()

    return message

def update_user(user, new_password):
    c, conn = sqlite_connect()
    try:
        if c and conn:
            user = (new_password, user.username)
            update_query = 'UPDATE ' + USERS_TABLE + ' SET password=? WHERE username=?'
            c.execute(update_query, user)
            conn.commit()
            message = build_response('Usuario actualizado con exito!', 200)
        else:
            message = build_response('Error en los datos, verificar el usuario', 400)
    except sqlite3.Error as sqe:
        message = build_response('Error al intentar actualizar el cliente, es posible que alguno de los datos especificados ya exista', 400)
        LOG.error('Sqlite Error al actualizar ' + str(sqe))
        LOG.error('Parametros recibidos: ' + str(user))
        LOG.error('Query: ' + str(update_query))

    finally:
        conn.close()

    return message


def delete_client(id):
    c, conn = sqlite_connect()
    try:
        if c and conn:
            if id is not None and id:
                delete_query = "DELETE FROM " + CLIENTS_TABLE + " WHERE id='%s'"
                c.execute(delete_query % id)
                conn.commit()
                message = build_response('Cliente eliminado con exito!', 200)
            else:
                message = build_response('Error en los datos, verificar formato de MAIL y BASE DE DATOS', 400)
    except sqlite3.Error as sqe:
        message = build_response('Error al intentar borrar el cliente', 400)
        LOG.error('Sqlite Error al borrar ' + str(sqe))
        LOG.error('Query: ' + str(delete_query))

    finally:
        conn.close()

    return message

def delete_registered_user(id):
    c, conn = sqlite_connect()
    try:
        if c and conn:
            if id is not None and id:
                delete_query = "DELETE FROM " + USERS_TABLE + " WHERE id='%s'"
                c.execute(delete_query % id)
                conn.commit()
                message = build_response('Usuario eliminado con exito!', 200)
            else:
                message = build_response('Error al intentar eliminar usuario', 400)
    except sqlite3.Error as sqe:
        message = build_response('Error al intentar borrar el usuario de la base de datos', 400)
        LOG.error('Sqlite Error al borrar ' + str(sqe))
        LOG.error('Query: ' + str(delete_query))

    finally:
        conn.close()

    return message

def search_user(username):
    c, conn = sqlite_connect()
    data = None
    if username and isinstance(username, str):
        try:
            select_query = "SELECT * FROM "+ USERS_TABLE +" WHERE username LIKE '%s'"
            c.execute(select_query % username)
            data = c.fetchone()
        except sqlite3.Error as sqe:
            LOG.error('Sqlite Error al intentar recuperar registros de la db: ' + str(sqe))
            LOG.error('Query: ' + str(select_query))
            LOG.error('USER name: ' + str(data))

        finally:
            conn.close()

    return data

def search_user_by_id(id):
    c, conn = sqlite_connect()
    data = None
    if id and isinstance(id, int):
        try:
            select_query = "SELECT * FROM "+ USERS_TABLE +" WHERE id == '%s'"
            c.execute(select_query % id)
            data = c.fetchone()
        except sqlite3.Error as sqe:
            LOG.error('Sqlite Error al intentar recuperar registros de la db: ' + str(sqe))
            LOG.error('Query: ' + str(select_query))
            LOG.error('USER name: ' + str(data))

        finally:
            conn.close()

    return data