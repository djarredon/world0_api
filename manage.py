#!/usr/bin/env python
from flask_script import Manager

from world0 import create_app
from world0.database import Model, create_db_session
from world0.models import User


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

if __name__ == '__main__':
    manager.run()
