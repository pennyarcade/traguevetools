"""
    @TODO: Application Apidoc
"""

import pprint
import requests

from bottle import *

import Model
import local_settings
from contract_parser import contract_parser


"""
    Bottle Setup Section

    Setup Bottle framework
"""
# Bottle debug mode
debug(True)


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
    contract parser
"""
@route('/')
@view('contractparser.html.tpl')
def index():
    return dict(
        # result for display
        result=None,
        # form data to preset form for debugging
        inputdata='',
        # debug output
        output=None
    )


@route('/', method='POST')
@view('contractparser.html.tpl')
def index():
    return contract_parser(
        request.forms.get('textAreaContract')
    )


# run application
application = default_app()
