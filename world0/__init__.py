from flask import Flask
from flask_login import LoginManager

from world0.api import account_api
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

    app.db_session = create_db_session(app.config.get('DATABASE_URI'))

    app.register_blueprint(account_api, url_prefix='/api/v1/account')

    login_manager = LoginManager(app)

    @app.teardown_appcontext
    def teardown_appcontext(response):
        app.db_session.remove()

    return app
