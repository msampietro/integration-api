from flask import Flask, request, render_template, abort
from application_properties import *
from utils import build_response, encode_auth_token,decode_auth_token
import logging as LOG
from flask_wtf import CSRFProtect

from sqlite_connector import new_client, list_clients, get_database, get_user, update_client, delete_client
from odoo_connector import odoo_insert, get_userId, odoo_connect
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

@csrf.exempt
@app.route('/new_lead', methods=['POST'])
def insert_lead():
    try:
        json = request.json
        #page_name = json[PAGE_NAME]
        page_name = 'Directv'
        if page_name is not None and page_name:
            auth = request.headers[AUTHORIZATION]
            if auth and auth == API_KEY:
                database = get_database(page_name.lower())
                odooJson = transformToOdooJson(json)
                extra_values = list()
                extra_values.append((TYPE, TYPE_VALUE))
                extra_values.append((USER_ID, get_userId(database, get_user(page_name.lower()))))
                append_values_json(extra_values,json)
                odoo_insertion = odoo_insert(database, odooJson)
        else:
            abort(401)
    except Exception as e:
        abort(400)

    return build_response('Success',200)




@app.route('/edit_clients', methods=['GET'])
def get_clients():
    clients = list_clients()
    return render_template('index.html', clientedit=clients)


@app.route('/delete_client', methods=['POST'])
def delete_clients():
    id = request.form.get('id')
    return delete_client(id)

@app.route('/update_client', methods=['POST'])
def update_clients():
    empresa = request.form.get('empresa')
    db = request.form.get('db')
    usuario_lead = request.form.get('usuario_lead')
    id = request.form.get('id')
    return update_client(empresa, db, usuario_lead, id)


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

def append_values_json(extra_values,json):
    for v in extra_values:
        value = v[1]
        if value is not None and value:
            json[v[0]] = value
    return json

def getOdooKey(formKey):
    with open(MAPPINGS_FILE) as json_data:
        odooMapping = jsonlib.load(json_data)

    for key, values in odooMapping.items():
        if formKey == key:
            return values

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5151)

