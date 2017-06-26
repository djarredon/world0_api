from cerberus import Validator
from flask import current_app, request, jsonify
from functools import wraps


def extend(_dict, **kwargs):
    _dict.update(dict(**kwargs))
    return _dict


def bad_input(error, code=400):
    response = jsonify(error)
    response.status_code = code
    return response

api_error = lambda code=400, **error: bad_input(error, code)
form_error = lambda error: bad_input(dict(form=[error]))
app_error = lambda error, code=400: bad_input(dict(app=[error]), code)


def validate(schema):
    def templated(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            v = Validator(schema)
            result = v.validate(request.json)
            return f(*args, **kwargs) if result else api_error(**v.errors)
        return decorated
    return templated

re_validator = lambda re, msg: lambda f, v, e: e if re.match(v) else e(f, msg)

string = lambda **kwargs: extend(dict(**kwargs), type='string')
integer = lambda **kwargs: extend(dict(**kwargs), type='integer')
_list = lambda **kwargs: extend(dict(**kwargs), type='list')
_dict = lambda **kwargs: extend(dict(**kwargs), type='dict')
