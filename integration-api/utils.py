import re
from flask import jsonify
import logging

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

    return response
