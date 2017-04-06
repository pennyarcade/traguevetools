'''
    @TODO: Application Apidoc
'''

'''
    Imports section
    @TODO document sources
'''
from bottle import default_app, route, run, debug
import requests
import traceback
import pprint
import local_settings

'''
    Globals Section
    
    Put global definitions here for now. Likely to move to a config module soon.
'''



'''
    Bottle Setup Section

    Setup Bottle framework
'''
# Bottle debug mode
debug(True)
# automatically reload app if files changed
# run(reloader=True)


'''
    demo page
'''
@route('/')
def hello_world():
    return 'Hello from Bottle!'

'''
    get ore prices from jita and return as  
'''
@route('/csv/jitaores')
def hello_world():
    output = ''
    output += 'csv / jita ores' + "\n\n"

    headers = {
        # Eve Api Token is secret, sorry
        'Authorisation': local_settings.ApiToken
    }
    url = 'https://crest-tq.eveonline.com/market/10000002/orders/all/'

    # get all orders from Forge region
    response = requests.get(url, headers=headers)

    output += pprint.pformat(response.text, indent=4)

    return output


# run Application
application = default_app()

