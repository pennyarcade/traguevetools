"""
    @TODO: Application Apidoc
"""

from bottle import default_app, route, run, debug
import requests
import traceback
import pprint
import local_settings

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
    demo page
"""
@route('/')
def hello_world():
    return 'Hello from Bottle!'

"""
    get ore prices from jita and return as  
"""
@route('/csv/jitaores')
def csv_jitaores():
    output = ''
    output += 'csv / jita ores' + "<br>"

    headers = {
        # Eve Api Token is secret, sorry
        'Authorisation': local_settings.ApiToken
    }
    url = 'https://crest-tq.eveonline.com/market/10000002/orders/all/'

    # get all orders from Forge region
    response = requests.get(url, headers=headers)
    data = response.json()

    for item in data.items:
        output += '<p>' + pprint.pformat(item, indent=4) + '</p>'

    return output


# run Application
application = default_app()
