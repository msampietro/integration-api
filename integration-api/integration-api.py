from flask import Flask, request, jsonify
from application_properties import *
from sqlite_connector import new_client, sqlite_connect, get_database
from odoo_connector import odoo_connect

app = Flask(__name__)


@app.route('/')
def index():
    return 'Integration API'

@app.route('/new_client', methods=['POST'])
def create_client():
    company = request.form.get(EMPRESA_KEY)
    db = request.form.get(DB_KEY)
    user_lead = request.form.get(USUARIO_LEAD_KEY)
    if company is not None and db is not None and user_lead is not None:
        return new_client(company, db, user_lead)

    return 'Missing arguments or invalid Arguments'

@app.route('/new_lead', methods=['POST'])
def insert_lead():
    page_name = request.form.get('page_name')
    odoo_connection = odoo_connect(get_database(page_name.lower()))
    return str(odoo_connection)




if __name__ == '__main__':
    app.run()


