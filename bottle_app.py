'''
    @TODO: Application Apidoc
'''

'''
    Imports section
    @TODO document sources
'''
from bottle import default_app, route, run
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
bottle.debug(True)
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
    output += 'csv / jita ores'

    headers = {
        # Eve Api Token is secret, sorry
        'Authorisation': local_settings.ApiToken
    }

    response = requests.get()

    return output


# run Application
application = default_app()

