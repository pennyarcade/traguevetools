"""
    @TODO: Application Apidoc
"""

from bottle import request
from plugin.bottle_sslify import SSLify
from plugin.bottle_ssl import SSLWSGIRefServer
import plugin.canister as canister
from plugin.canister import session

from esipy import App
from esipy import EsiClient
from esipy import EsiSecurity
from esipy.exceptions import APIException
from esipy.cache import FileCache

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


def token_updater(token):
    session.data['oauth_token'] = token


# -----------------------------------------------------------------------
# ESIPY Init
# -----------------------------------------------------------------------
# create the app
esiapp = App.create(
    local_settings.eve_oauth_swagger_json
)

esicache = FileCache(
    path=localsettings.eve_oauth_cache_dir
)

# init the security object
esisecurity = EsiSecurity(
    app=esiapp,
    redirect_uri=local_settings.eve_oauth_callback,
    client_id=local_settings.eve_oauth_client_id,
    secret_key=local_settings.eve_oauth_secret_key,
)

# init the client
esiclient = EsiClient(
    security=esisecurity,
    retry_requests=True,
    cache=esicache,
    headers={
        'User-Agent': local_settings.eve_oauth_client_name
    }
)

# -----------------------------------------------------------------------
# Login / Logout Routes
# -----------------------------------------------------------------------
@route('/login/')
def login():
    """ this redirects the user to the EVE SSO login """
    return redirect(esisecurity.get_auth_uri(
        scopes=local_settings.eve_oauth_scopes
    ))


@app.route('/logout/')
@login_required
def logout():
    # Todo: Implement logout
    return redirect('/')


@route('/authcallback/')
def callback():
    """ This is where the user comes after he logged in SSO """
    # get the code from the login process
    code = request.args.get('code')

    # now we try to get tokens
    try:
        auth_response = esisecurity.auth(code)
    except APIException as e:
        return 'Login EVE Online SSO failed: %s' % e, 403

    # we get the character informations
    cdata = esisecurity.verify()

    # if the user is already authed, we log him out
    if current_user.is_authenticated:
        # Todo: Implement logout
        pass

    # now we check in database, if the user exists
    # actually we'd have to also check with character_owner_hash, to be
    # sure the owner is still the same, but that's an example only...
    try:
        user = User.query.filter(
            User.character_id == cdata['CharacterID'],
        ).one()

    except NoResultFound:
        user = User()
        user.character_id = cdata['CharacterID']

    user.character_owner_hash = cdata['CharacterOwnerHash']
    user.character_name = cdata['CharacterName']
    user.update_token(auth_response)

    # now the user is ready, so update/create it and log the user
    try:
        db.session.merge(user)
        db.session.commit()

        login_user(user)
        session.permanent = True

    except:
        logger.exception("Cannot login the user - uid: %d" % user.character_id)
        db.session.rollback()
        logout_user()

    return redirect('/')


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
