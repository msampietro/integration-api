from flask import Flask, request, render_template
from application_properties import *
from sqlite_connector import new_client, get_database
from odoo_connector import odoo_connect
from utils import build_response
import logging as LOG
from flask_wtf import CSRFProtect

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
    page_name = request.form.get('page_name')
    odoo_connection = odoo_connect(get_database(page_name.lower()))
    return str(odoo_connection)



if __name__ == '__main__':
    app.run()


