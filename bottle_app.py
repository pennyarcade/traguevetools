"""
    @TODO: Application Apidoc
"""

from bottle import *
from plugin.bottle_sslify import SSLify
from plugin.bottle_ssl import SSLWSGIRefServer
from requests_oauthlib import OAuth2Session
import plugin.canister as canister
from plugin.canister import session

import logging
import os

from controller.contract_parser import ContractController
from controller.development import DevelopmentController
from controller.donations import DonationsController
from controller.login import login

from model import Model
import local_settings


"""
    Bottle Setup Section

    Setup Bottle framework
"""
# Bottle debug mode
debug(True)
# run application
application = default_app()

# register and configure canister plugin for auth and sessions
application.config.load_config('config.cfg')
application.install(canister.Canister())

# register controllers
ContractController.register(application)
DevelopmentController.register(application)
DonationsController.register(application)


logging.basicConfig(
        filename='logs/requests.log',
        level=logging.INFO,
        format="[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
        datefmt="%H:%M:%S"
    )
logger = logging.getLogger('peewee')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.FileHandler('logs/peewee.log'))
logger = logging.getLogger('oauthlib')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.FileHandler('logs/oauth.log'))


"""
    hooks for database integration
"""
@hook('before_request')
def _connect_db():
    Model.db.connect()


@hook('after_request')
def _close_db():
    if not Model.db.is_closed():
        Model.db.close()


"""
    redirect to index page
"""


@route('/', method='ANY')
def index():
    redirect('/contract/')


@route('/login/')
def sso_login():
    esi = OAuth2Session(
        local_settings.eve_oauth_client_id,
        auto_refresh_url=local_settings.eve_oauth_token_exchange,
        auto_refresh_kwargs={

        },
        redirect_uri=local_settings.eve_oauth_callback,
        scope=local_settings.eve_oauth_scopes,
        token_updater=token_updater
    )
    authorization_url, state = esi.authorization_url(
        local_settings.eve_oauth_login
    )

    # State is used to prevent CSRF, keep this for later.
    session.data['oauth_state'] = state
    return redirect(authorization_url)


@route('/authcallback/')
def authenticate():
    esi = OAuth2Session(
        local_settings.eve_oauth_client_id,
        redirect_uri=local_settings.eve_oauth_callback,
        scope=local_settings.eve_oauth_scopes
    )
    token = esi.fetch_token(
        local_settings.eve_oauth_token_exchange,
        client_secret=local_settings.eve_oauth_secret_key,
        authorization_response=request.url
    )

    session.data['oauth_token'] = token


def token_updater(token):
    session.data['oauth_token'] = token


if local_settings.environment != "prod":
    @route('/static/<filename:path>')
    def static(filename):
        import os
        path = os.path.join(
            os.path.abspath(
                os.path.dirname(__file__)
            ),
            'static/'
        )
        return static_file(filename, root=path)


if __name__ == "__main__":
    os.environ['DEBUG'] = '1'
    srv = SSLWSGIRefServer(host="127.0.0.1", port=8090)
    run(server=srv)
else:
    SSLify(application)
