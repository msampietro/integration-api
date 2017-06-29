import re
from application_properties import *

def validate_regex(text, expression):
    is_valid = False
    try:
        if re.match(expression, text):
            is_valid = True
    except Exception as e:
        print('error during regex validation: '+ str(e))
    return is_valid

