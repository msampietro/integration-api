from flask import Flask, request, render_template, abort, redirect, url_for
from application_properties import *
from application_constants import *
from utils import build_response, append_values_json, transform_odoo_json, match_regex, compound_json_values, append_values
import logging as LOG
from flask_wtf import CSRFProtect
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from sqlite_connector import new_client, list_clients, get_database, \
   update_client, delete_client, update_user, new_user, list_users, delete_registered_user
from odoo_connector import odoo_insert
from user_form import User



app = Flask(__name__)
app.secret_key = SECRET_KEY
csrf = CSRFProtect()
csrf.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
LOG.basicConfig(filename=LOG_FILE, level=LOG.ERROR)


@app.route('/mad/clients', methods=['GET'])
@login_required
def get_clients():
    clients = list_clients()
    return render_template('index.html', clientedit=clients)

@app.route('/mad', methods=['POST', 'GET'])
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

@app.route('/mad/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/mad/new_client', methods=['POST'])
@login_required
def create_client():
    company = request.form.get(EMPRESA_KEY)
    db = request.form.get(DB_KEY)
    #user_lead = request.form.get(USUARIO_LEAD_KEY)

    if company is not None and db is not None:
        if company and db:
            return new_client(company, db)

    return build_response('Hay argumentos faltantes o incorrectos en la peticion', 400)

@csrf.exempt
@app.route('/mad/new_lead', methods=['POST'])
def insert_lead():
    try:
        json = request.json
        LOG.info("Nuevo lead recibido: ", json)
        page_name = json[PAGE_NAME]
        titulo = json[TITULO]
        page_name = match_regex(page_name, PAGE_NAME_REGEX)
        if page_name is not None and titulo is not None and page_name and titulo:
            auth = request.headers[AUTHORIZATION]
            if auth and auth == API_KEY:
                database = get_database(page_name[0].lower())
                odoo_compound = compound_json_values(json, COMPOUND_FILE)
                odoo_json = transform_odoo_json(odoo_compound, MAPPINGS_FILE)
                extra_values = list()
                extra_values.append((TYPE, TYPE_VALUE))
                append_values_json(extra_values, json)
                if len(page_name) > 1:
                    del page_name[0]
                    for v in page_name:
                        append_values(v, odoo_json)
                odoo_insert(database, odoo_json)
            else:
                abort(401)
        else:
            LOG.ERROR("El page_name es invalido o falta el campo TITULO en el json")
            abort(401)
    except Exception as e:
        LOG.error("Exception al intentar insertar un lead " + str(e))
        abort(400)
    return build_response('Success', 200)

@app.route('/mad/delete_client', methods=['POST'])
@login_required
def delete_clients():
    id = request.form.get(ID_KEY)
    if id is not None and id:
        id_int = int(id)
        return delete_client(id_int)
    return build_response("El cliente seleccionado no pudo ser borrado",400)

@app.route('/mad/create', methods=['POST'])
@login_required
def create_user():
    username = request.form['user_new']
    password1 = request.form['new_password_create']
    password2 = request.form['new_password2_create']
    user = User.get(username)
    if not user:
        if password1 == password2 and password1 and password2:
            return new_user(username, password2)
        return build_response('Error al crear usuario, las claves no son iguales o estan vacias', 400)
    return build_response('Error al crear usuario, ese usuario ya existe', 400)

@app.route('/mad/change', methods=['GET','POST'])
@login_required
def change_user():
    if request.method == 'GET':
        users = list_users()
        return render_template('change.html', users=users)
    else:
        username = request.form['user_now']
        password = request.form['password_now']
        password1 = request.form['new_password']
        password2 = request.form['new_password2']
        user = User.get(username)
        if user:
            if user.password == password:
                if password1 == password2 and password and password2 and password1:
                    return update_user(user, password2)
                return build_response('Especificar contraseña', 400)
            return build_response('Error al actualizar usuario, contraseña actual incorrecta', 400)
    return build_response('Error al actualizar usuario, no hay coincidencia en las claves',400)

@app.route('/mad/update_client', methods=['POST'])
@login_required
def update_clients():
    empresa = request.form.get(EMPRESA_KEY)
    db = request.form.get(DB_KEY)
    id = request.form.get(ID_KEY)
    return update_client(empresa, db, id)

@app.route('/mad/delete_user', methods=['POST'])
@login_required
def delete_user():
    id = request.form.get(ID_KEY)
    if id is not None and id:
        id_int = int(id)
        user = User.get_object(id_int)
        if user.username == current_user.username:
            return build_response('El usuario actual no puede ser eliminado', 400)
        else:
            return delete_registered_user(id)
    return build_response('Error al intentar eliminar el usuario', 400)

@login_manager.user_loader
def load_user(id):
    return User.get_object(id)


if __name__ == '__main__':
    app.run(host='0.0.0.0')