from flask import Flask, request, render_template, abort, redirect, url_for
from application_properties import *
from utils import build_response, append_values_json, transform_odoo_json
import logging as LOG
from flask_wtf import CSRFProtect
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from sqlite_connector import new_client, list_clients, get_database, \
    get_user, update_client, delete_client
from odoo_connector import odoo_insert, get_user_id, odoo_connect
from user_form import User



app = Flask(__name__)
app.secret_key = SECRET_KEY
csrf = CSRFProtect()
csrf.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
LOG.basicConfig(filename=LOG_FILE, level=LOG.ERROR)


@app.route('/clients', methods=['GET'])
@login_required
def get_clients():
    clients = list_clients()
    return render_template('index.html', clientedit=clients)

@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        if current_user.is_authenticated:
            return redirect(url_for('get_clients'))
        else:
            return render_template('login.html')
    else:
        username = request.form['username']
        password = request.form['password']
        user = User.get(username)
        if user:
            if user.password == password:
                login_user(user)
                return redirect(url_for('get_clients'))
        return render_template('login.html', message='Credenciales invalidas')

@app.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/new_client', methods=['POST'])
@login_required
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
        page_name = json[PAGE_NAME]
        if page_name is not None and page_name:
            auth = request.headers[AUTHORIZATION]
            if auth and auth == API_KEY:
                database = get_database(page_name.lower())
                odoo_json = transform_odoo_json(json)
                extra_values = list()
                extra_values.append((TYPE, TYPE_VALUE))
                append_values_json(extra_values, json)
                odoo_insert(database, odoo_json)
            else:
                abort(401)
        else:
            abort(401)
    except Exception as e:
        abort(400)
    return build_response('Success', 200)

@app.route('/delete_client', methods=['POST'])
@login_required
def delete_clients():
    id = request.form.get('id')
    return delete_client(id)

@app.route('/update_client', methods=['POST'])
@login_required
def update_clients():
    empresa = request.form.get('empresa')
    db = request.form.get('db')
    usuario_lead = request.form.get('usuario_lead')
    id = request.form.get('id')
    return update_client(empresa, db, usuario_lead, id)

@login_manager.user_loader
def load_user(id):
    return User.get_object(id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

