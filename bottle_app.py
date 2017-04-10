"""
    @TODO: Application Apidoc
"""

from bottle import *
import peewee
import requests
import traceback
import pprint
import local_settings
import StringIO

import Model

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
    # saves debug output
    output = ''
    # list of items from Input
    item_list = []

    raw_data = request.forms.get('textAreaContract')
    for line in StringIO.StringIO(str(raw_data)):
        # inventory etries copied from eve are separated by tab caracters
        parts = line.split("\t")

        # catch error when not enough parts are found
        try:
            amount = parseint(parts[1])

            #stack items to remove duplicates
            found = False
            for index, line in enumerate(item_list):
                if line['typeName'] == parts[0].strip():
                    line['amount'] += amount
                    found = True
                    item_list[index] = line

            # add new item only if it is not in the list yet
            if not found:
                # get item ID from DB
                item = Model.InvType.get(
                    Model.InvType.typeName == parts[0].strip()
                )

                # build list entry
                item_list.append({
                    'typeName': parts[0].strip(),
                    'amount': amount,
                    'typeID': item.typeID,
                    'description': item.description
                })

        except IndexError:
            # dump parsing errors to debug output
            output += ''.join(
                traceback.format_exc()
            )

    # get all Jita offers
    headers = {
        # Eve Api Token is secret, sorry
        'Authorisation': local_settings.ApiToken
    }
    endpoint_url = 'https://crest-tq.eveonline.com/market/10000002/orders/all/'

    # get all orders from Forge region
    api_response = requests.get(endpoint_url, headers=headers)
    data = api_response.json()

    output += pprint.pformat(data)

    '''
    #Filter highest bids
    for index, item in enumerate(item_list):
        buy_prices = list()
        sell_prices = list()
        for line in data:
            if item['typeID'] == line['type'] and line['stationID'] == jitaStationId:
                if line['buy']:
                    buy_prices.append(line['price'])
                else:
                    sell_prices.append(line['price'])

        # enrich item list with price data
        item['max_buy_price'] = max(buy_prices)
        item['min_buy_price'] = min(buy_prices)
        item['max_sell_price'] = max(sell_prices)
        item['min_sell_price'] = min(sell_prices)
        item_list[index] = item
    '''

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

def parseint(string):
    """
        parse string to integer in a consistent way
    """
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
