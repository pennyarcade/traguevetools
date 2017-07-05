"""
    @TODO: Application Apidoc
"""

from bottle import *
from plugin.bottle_sslify import SSLify
from plugin.bottle_ssl import SSLWSGIRefServer
import plugin.canister as canister
import logging

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
        format='%(asctime)s %(levelname)s %(message)s'
    )
logger = logging.getLogger('peewee')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.FileHandler('logs/peewee.log'))


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
@route('/authcallback/')
def login():
    return login(request=request, response=response)


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
    srv = SSLWSGIRefServer(host="127.0.0.1", port=8090)
    run(server=srv)
else:
    SSLify(application)
