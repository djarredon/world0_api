"""User login/logout/profile etc API"""
from flask import Blueprint, current_app, jsonify, request as r
from flask_login import (
    login_user, logout_user, login_required, current_user
)

from world0.marshal import marshal_current_user
from world0.models import User
from world0.schemas import login_schema, register_schema
from world0.util import form_error, validate


account_api = Blueprint('account_api', __name__)

@account_api.route('/register', methods=['POST'])
@validate(register_schema)
def register():
    """
    Register a user account.
    """
    user = User(
        username=r.json['username'],
        email=r.json['email'],
        password=r.json['password']
    ).save()
    login_user(user)
    return jsonify(marshal_current_user(user))

@account_api.route('/login', methods=['POST'])
@validate(login_schema)
def login():
    """
    Authenticate as a user.
    """
    user = User.get_by_email_or_username(r.json['username'].lower())
    if user is not None and user.check_password(r.json['password']):
        login_user(user)
        return jsonify(marshal_current_user(user))
    return form_error('Invalid username/password.')

@account_api.route('/logout', methods=['POST'])
@login_required
def logout():
    """
    Deauthenticate user.
    """
    logout_user()
    return '', 200
