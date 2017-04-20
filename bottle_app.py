"""
    @TODO: Application Apidoc
"""

from bottle import *

from controller.contract_parser import contract_parser
from model import Model
import local_settings

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


# run application
application = default_app()

if __name__ == "__main__":
    run()