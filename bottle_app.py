"""
    @TODO: Application Apidoc
"""

from bottle import *
import bottle_mysql
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

# install mysql plugin
mysql_plugin = bottle_mysql.Plugin(
    dbuser=local_settings.MySqlUser,
    dbpass=local_settings.MySqlPwd,
    dbname=local_settings.MySqlName,
    dbhost=local_settings.MySqlHost
)


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
def index(db):
    output = ''
    item_list = []
    item_row = None

    raw_data = request.forms.get('textAreaContract')
    for line in StringIO.StringIO(str(raw_data)):
        parts = line.split("\t")

        # catch error when not enough parts are found
        try:
            amount = parseint(parts[1])

            # Todo: get item ID from DB
            item_id = None
            db.execute('SELECT * FROM invTypes WHERE typeName = %s' % parts[0].strip())
            row = db.fetchone()

            if row:
                item_id = row[0]
                irem_row = row

            # build list entry
            item_list.append([parts[0], item_id, amount, row])
        except Exception:
            output += traceback.format_exception()
            # Todo: error handling
            raise

    # Todo: Sort and stack items

    # Todo: get all Jita offers

    # Todo: Filter highest bids

    # Todo: cache highest bids 15 mins

    # Todo: enrich item list with price data

    output += pprint.pformat(item_list)

    # Todo: format output data?

    return dict(
        # result for display
        result=None,
        # form data to preset form for debugging
        inputdata=raw_data,
        # debug output
        output=output
    )

"""
    parse string to integer in a consistent way
"""
def parseint(string):
    try:
        amount = int(string)
    except ValueError:
        # not repackaged things
        amount = 1
    return amount


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


# run application
application = default_app()
application.install(mysql_plugin)
