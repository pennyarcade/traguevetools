"""
    @TODO: Application Apidoc
"""

from bottle import *
import requests
import traceback
import pprint
import local_settings
import StringIO

"""
    Globals Section
    
    Put global definitions here for now. Likely to move to a config module soon.
"""
jitaStationId = '60003466'
forgeRegionId = '10000002'

"""
    Bottle Setup Section

    Setup Bottle framework
"""
# Bottle debug mode
debug(True)
# automatically reload app if files changed
# run(reloader=True)


"""
    contract parser
"""
@route('/')
@view('contractparser.html')
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
@view('contractparser.html')
def index():
    output = ''
    item_list = []

    raw_data = request.forms.get('textAreaContract')
    for line in StringIO.StringIO(str(raw_data)):
        parts = line.split("\t")
        try:
            amount = int(parts[1])
        except ValueError:
            amount = None

        item_list.append((parts[0], amount))

    output += pprint.pformat(item_list)

    return dict(
        # result for display
        result=None,
        # form data to preset form for debugging
        inputdata=raw_data,
        # debug output
        output=output
    )


"""
    get ore prices from jita and return as csv  
"""
@route('/csv/jitaores')
def csv_jitaores():
    output = ''
    output += 'csv / jita ores' + "<br>"

    headers = {
        # Eve Api Token is secret, sorry
        'Authorisation': local_settings.ApiToken
    }
    endpoint_url = 'https://crest-tq.eveonline.com/market/10000002/orders/all/'

    # get all orders from Forge region
    api_response = requests.get(endpoint_url, headers=headers)
    data = api_response.json()

    for item in data['items']:
        output += '<p>' + pprint.pformat(item, indent=4) + '</p>'

    return output


# run Application
application = default_app()
