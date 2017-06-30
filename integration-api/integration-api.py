from flask import Flask, request, jsonify
from application_properties import *
from sqlite_connector import new_client, sqlite_connect, get_database
from odoo_connector import odoo_connect
import json

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
    page_name = request.json.get('page_name')
    odoo_connection = odoo_connect(get_database(page_name.lower()))
    json = request.get_json()
    print(json)
    odooJson = transformToOdooJson(json)
    print(odooJson)
    return str(odoo_connection)

def transformToOdooJson(json):
    for key, values in json.copy().items():
        k = getOdooKey(key)
        if k != None:
            if k == key:
                json[k] = json[key]
            else:
                json[k] = json[key]
                del json[key]
        else:
            del json[key]
    return json

def getOdooKey(formKey):
    with open('./odoo_mappings.json') as json_data:
        odooMapping = json.load(json_data)

    for key, values in odooMapping.items():
        if formKey == key:
            return values


if __name__ == '__main__':
    app.run()


