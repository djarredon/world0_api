import re

from world0.models import User
from world0.util import (
    extend, re_validator, string, integer, _list, _dict
)


def username_unique_validator(f, v, e):
    if User.get_by_username(v):
        e(f, 'username already in use')

email_format_validator = re_validator(
    re.compile(r'^.+@([^.@][^@]+)$', re.IGNORECASE),
    'value must be a valid email'
)
def email_unique_validator(f, v, e):
    if User.get_by_email(v):
        e(f, 'email already in use')

register_schema = dict(
    username=string(required=True, empty=False, maxlength=255,
        validator=username_unique_validator),
    email=string(required=True, maxlength=255,
        validator=[email_unique_validator, email_format_validator]),
    password=string(required=True, empty=False)
)

login_schema = dict(
    username=string(required=True, empty=False, maxlength=255),
    password=string(required=True, empty=False)
)
