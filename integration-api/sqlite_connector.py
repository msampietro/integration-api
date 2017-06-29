import sqlite3
from application_properties import *
from utils import validate_regex

def sqlite_connect():
    try:
        conn = sqlite3.connect(SQLITE_PATH)
        c = conn.cursor()
        return c, conn
    except sqlite3.Error as sqe:
        print('sqlite error during connection' + str(sqe))
        return None


def new_client(company, db, user_lead):
    c, conn = sqlite_connect()
    try:
        if company and db and user_lead:
            if isinstance(company, str) and validate_regex(db, DATABASE_REGEX) and validate_regex(user_lead, EMAIL_REGEX):
                client = (company, db, user_lead)
                insert_query = 'INSERT INTO ' + CLIENTS_TABLE + ' VALUES (NULL, ?, ?, ?)'
                c.execute(insert_query, client)
                conn.commit()
                return('New Client Inserted Successfully')
    except sqlite3.Error as sqe:
        print('sqlite error during insert ' + str(sqe))
        return 'Error during Client Creation'

    finally:
        conn.close()

    return 'Invalid or Empty Values'

def get_database(client_name):
    if client_name and isinstance(client_name, str):
        try:
            select_query = "SELECT "+ DB_KEY +" FROM " + CLIENTS_TABLE + " WHERE " + EMPRESA_KEY + " = '%s'"
            c, conn = sqlite_connect()
            c.execute(select_query % client_name)
            return c.fetchone()
        except sqlite3.Error as sqe:
            print('sqlite error reading database: ' + str(sqe))

        finally:
            conn.close()

    return 'Invalid or Empty Values'
