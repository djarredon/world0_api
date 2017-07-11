#!/usr/bin/env python
from cerberus import Validator
from flask_script import Manager

from world0 import create_app
from world0.database import Model, create_db_session
from world0.models import User
from world0.schemas import register_schema


app = create_app()

manager = Manager(app)

@manager.command
def create_db():
    """Create the database."""
    try:
        from config import DATABASE_URI
    except:
        from configdist import DATABASE_URI
    db_session = create_db_session(DATABASE_URI)
    Model.metadata.create_all(bind=db_session.bind)

@manager.command
@manager.option('-u', '--username', help='Username')
@manager.option('-e', '--email', help='Email')
@manager.option('-p', '--password', help='Password')
def add_user(username, email, password):
    validator = Validator(register_schema)
    validator.validate(dict(
        email=email,
        username=username,
        password=password
    ))
    if validator.errors:
        print(validator.errors)
        exit()
    user = User(email=email, username=username, password=password).save()
    print('Successfully added %s' % user)

if __name__ == '__main__':
    manager.run()
