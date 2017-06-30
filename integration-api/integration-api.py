from flask import Flask, request, render_template
from application_properties import *
from utils import build_response
import logging as LOG
from flask_wtf import CSRFProtect

from sqlite_connector import new_client, sqlite_connect, get_database
from odoo_connector import odoo_connect, odoo_insert
import json


app = Flask(__name__)
app.secret_key = SECRET_KEY
csrf = CSRFProtect()
csrf.init_app(app)
LOG.basicConfig(filename=LOG_FILE, level=LOG.ERROR)

@app.route('/')
def index():
    return render_template('index.html', name='index')

@app.route('/new_client', methods=['POST'])
def create_client():
    company = request.form.get(EMPRESA_KEY)
    db = request.form.get(DB_KEY)
    user_lead = request.form.get(USUARIO_LEAD_KEY)

    if company is not None and db is not None and user_lead is not None:
        if company and db and user_lead:
            return new_client(company, db, user_lead)

    return build_response('Hay argumentos faltantes o incorrectos en la peticion', 400)

@app.route('/new_lead', methods=['POST'])
def insert_lead():
    json = request.get_json()
    page_name = json[PAGE_NAME]

    odooJson = transformToOdooJson(json)
    odoo_insertion = odoo_insert(get_database(page_name.lower()), odooJson, page_name)
    return str(odoo_insertion)

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


