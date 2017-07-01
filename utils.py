import re
from flask import jsonify
import logging
import datetime
from application_properties import *
import jwt
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

def encode_auth_token(user_id):
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
            'iat': datetime.datetime.utcnow(),
            'sub': user_id
        }
        return jwt.encode(
            payload,
            SECRET_KEY,
            algorithm='HS256'
        )
    except Exception as e:
        return e


def decode_auth_token(auth_token):
    try:
        payload = jwt.decode(auth_token, SECRET_KEY)
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'