import re
from flask import jsonify
import logging
import json as jsonlib
from application_properties import *
from application_constants import *

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

def match_regex(text, expression):
    result = None
    try:
        result = re.findall(expression, text)
    except Exception as e:
        LOG.error('Error durante la validacion del Regex: '+ str(e))
        LOG.error('Expression: ' + str(expression) +' - Text: ' + str(text))

    return result

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

def transform_odoo_json(json, file):
    for key, values in json.copy().items():
        k = get_odoo_key(key, file)
        if k != None:
            if k == key:
                json[k] = str(json[key])
            else:
                json[k] = str(json[key])
                del json[key]
        else:
            del json[key]

    return json

def compound_json_values(json, file):
    for key, values in json.copy().items():
        k = get_odoo_key(key, file)
        if k != None:
            suffix = json[key]
            if json[k] and json[k] is not None:
                json[k] = suffix + str(json[k])
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

def append_values(value, json):
    if value is not None and value:
        try:
            if json[APPEND_FIELD] is not None:
                json[APPEND_FIELD] = json[APPEND_FIELD] + APPEND_SEPARATOR + value
        except KeyError:
            json[APPEND_FIELD] = value
    return json

def get_odoo_key(formKey, file):
    with open(file) as json_data:
        odoo_mapping = jsonlib.load(json_data)

    for key, values in odoo_mapping.items():
        if formKey == key:
            return values