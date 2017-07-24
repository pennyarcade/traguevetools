# -*- encoding: utf-8 -*-
import logging

from flask import Flask
from flask import render_template
from flask_login import LoginManager

from flask_login import current_user
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import local_config as config
from evetools.api.esi import esiapp, esiclient, esisecurity
from evetools.model.user import User

from evetools.blueprints.login import login

# logger stuff
logger = logging.getLogger(__name__)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
console.setFormatter(formatter)
logger.addHandler(console)

# init app and load conf
app = Flask(__name__)
app.config.from_object(config)
app.register_blueprint(login, url_prefix='/sso')

# init db
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# init flask login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


# -----------------------------------------------------------------------
# Flask Login requirements
# -----------------------------------------------------------------------
@login_manager.user_loader
def load_user(character_id):
    """ Required user loader for Flask-Login """
    return User.query.get(character_id)


# -----------------------------------------------------------------------
# Index Routes
# -----------------------------------------------------------------------
@app.route('/')
def index():
    wallet = None

    # if the user is authed, get the wallet content !
    if current_user.is_authenticated:
        # give the token data to esisecurity, it will check alone
        # if the access token need some update
        esisecurity.update_token(current_user.get_sso_data())

        op = esiapp.op['get_characters_character_id_wallets'](
            character_id=current_user.character_id
        )
        wallet = esiclient.request(op)

    return render_template('base.html', **{
        'wallet': wallet,
    })
