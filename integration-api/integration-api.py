from flask import Flask, request, render_template
from application_properties import *
from utils import build_response
import logging as LOG
from flask_wtf import CSRFProtect

from sqlite_connector import new_client, list_clients, get_database, get_clients
from odoo_connector import odoo_connect, odoo_insert
import json as jsonlib


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

    page_name = request.form.get(PAGE_NAME)
    dictt = dict(request.form)
    json = jsonlib.dumps(dictt, ensure_ascii=False)

    nombre = dictt['nombre'][0]

    odooJson = transformToOdooJson(json)
    odoo_insertion = odoo_insert(get_database(page_name.lower()), odooJson, page_name)
    return str(odoo_insertion)

@app.route('/edit_clients', methods=['GET'])
def get_clients():
    clients = list_clients()
    return render_template('index.html', clientedit=clients)


@app.route('/delete_clients', methods=['POST'])
def delete_clients():
    id = request.form.get('res')
    return id


def transformToOdooJson(json):
    json_copy = json.copy().items()
    for key, values in json_copy:
        k = getOdooKey(key)
        if k != None:
            if k == key:
                json_copy[k] = json_copy[key]
            else:
                json_copy[k] = json_copy[key]
                del json_copy[key]
        else:
            del json_copy[key]
    return json_copy

def getOdooKey(formKey):
    with open(MAPPINGS_FILE) as json_data:
        odooMapping = jsonlib.load(json_data)

    for key, values in odooMapping.items():
        if formKey == key:
            return values

if __name__ == '__main__':
    app.run(port=5151)


