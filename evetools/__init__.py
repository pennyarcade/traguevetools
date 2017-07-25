# -*- encoding: utf-8 -*-
import logging

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import local_config as config
# from evetools.api.esi import esiapp, esiclient, esisecurity
# from evetools.model.user import User
# from evetools.api.login_manager import login_manager

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


# defer loading to resolve circular dependencies >-<
from evetools.blueprints.login import login
from evetools.blueprints.index import index

app.register_blueprint(login, url_prefix='/sso')
app.register_blueprint(index)
