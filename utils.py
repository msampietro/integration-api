import re
from flask import jsonify
import logging
import json as jsonlib
from application_properties import *

LOG = logging.getLogger(__name__)


def validate_regex(text, expression):
    is_valid = False
    try:
        if re.match(expression, text):
            is_valid = True
    except Exception as e:
        LOG.error('Error durante la validacion del Regex: '+ str(e))
        LOG.error('Expression: ' + str(expression) +' - Text: ' + str(text))

    return is_valid

def build_response(message, code):
    if code == 400:
        response = jsonify(
            details=message,
            message='Bad Request',
            status=400,
        )
    elif code == 200:
        response = jsonify(
            details=message,
            message='OK. The request has succeeded',
            status=200

        )
    elif code == 401:
        response = jsonify(
            details=message,
            message='FORBIDDEN. Invalid Credentials',
            status=200

        )

    return response

def transform_odoo_json(json):
    for key, values in json.copy().items():
        k = get_odoo_key(key)
        if k != None:
            if k == "cod_tel":
                if 'phone' in json:
                    json['phone'] = values + json['phone']
                    del json['cod_area_tel']
                else:
                    json['telefono'] = values + json['telefono']
                    del json['cod_area_tel']
            else:
                if k == 'cod_cel':
                    if 'mobile' in json:
                        json['mobile'] = values + json['mobile']
                        del json['cod_area_cel']
                    else:
                        json['celular'] = values + json['celular']
                        del json['cod_area_cel']
                else:
                    if k == key:
                        json[k] = json[key]
                    else:
                        json[k] = json[key]
                        del json[key]
        else:
            del json[key]

    return json

def append_values_json(extra_values, json):
    for v in extra_values:
        value = v[1]
        if value is not None and value:
            json[v[0]] = value
    return json

def get_odoo_key(formKey):
    with open(MAPPINGS_FILE) as json_data:
        odoo_mapping = jsonlib.load(json_data)

    for key, values in odoo_mapping.items():
        if formKey == key:
            return values