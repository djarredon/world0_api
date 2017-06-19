from flask import Flask

from world0.database import create_db_session


def create_app(config=None):
    """
    Setup flask app with blueprints, extensions and other necessary additions.
    """
    app = Flask(__name__)

    # Configure Flask
    app.config.from_object('configdist')
    try:
        app.config.from_object('config')
    except:
        pass
    if config:
        app.config.from_object(config)

    @app.teardown_appcontext
    def teardown_appcontext(response):
        app.db_session.remove()

    return app
