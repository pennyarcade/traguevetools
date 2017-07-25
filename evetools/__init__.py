# -*- encoding: utf-8 -*-
import logging

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

import local_config as config

# logger stuff
evelogger = logging.getLogger(__name__)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
console.setFormatter(formatter)
evelogger.addHandler(console)


# init app and load conf
app = Flask(__name__)
app.config.from_object(config)

# init db
evedb = SQLAlchemy(app)
migrate = Migrate(app, evedb)

# init flask login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


# -----------------------------------------------------------------------
# Flask Login requirements
# -----------------------------------------------------------------------
@login_manager.user_loader
def load_user(character_id):
    from evetools.model.user import User

    """ Required user loader for Flask-Login """
    return User.query.get(character_id)


# -----------------------------------------------------------------------
# Register Blueprints
# -----------------------------------------------------------------------
# defer loading to resolve circular dependencies >-<
def register_blueprints():
    from evetools.blueprints.login import login
    from evetools.blueprints.index import index

    app.register_blueprint(login, url_prefix='/sso')
    app.register_blueprint(index)

# register blueprints
register_blueprints()
