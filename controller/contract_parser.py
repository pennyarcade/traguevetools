import StringIO
import pprint
import requests
import traceback

import common_settings
import local_settings
from model import Model


def contract_parser(raw_data):
    """
    
    :param raw_data: 
    :return: 
    """
    # saves debug output
    output = ''
    # list of items from Input
    item_list = []
    for line in StringIO.StringIO(str(raw_data)):
        # inventory etries copied from eve are separated by tab caracters
        parts = line.split("\t")

        # catch error when not enough parts are found
        try:
            amount = parseint(parts[1])

            found = stack_items(item_list, amount, parts)

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

    # Filter highest bids
    for index, item in enumerate(item_list):
        buy_prices = list()
        sell_prices = list()

        market_url = '%s/market/%s/orders/?type=%s/inventory/types/%s/' % (
            common_settings.baseUrl,
            common_settings.forgeRegionId,
            common_settings.baseUrl,
            item['typeID']
        )

        data = getJsonData(market_url)

        if 'items' in data:
            enrich_item(data, item, buy_prices, sell_prices)

            item_list[index] = item
        else:
            output += pprint.pformat(data)

    # output += pprint.pformat(item_list)
    result = {
        'price_table': item_list,
        'sum': sum(item['corp_buy_total'] for item in item_list)
    }
    response_dict = dict(
        # result for display
        result=result,
        # form data to preset form for debugging
        inputdata=raw_data,
        # debug output
        output=output
    )
    return response_dict


def stack_items(item_list, amount, parts):
    """
    stack items to remove duplicates

    :param item_list: 
    :param amount: 
    :param parts: 
    :return: 
    """
    found = False
    for index, line in enumerate(item_list):
        if line['typeName'] == parts[0].strip():
            line['amount'] += amount
            found = True
            item_list[index] = line

    return found


def enrich_item(data, item, buy_prices, sell_prices):
    """
        :param data: 
        :param item: 
        :param buy_prices: 
        :param sell_prices: 
        :return: void
    """
    for line in data['items']:
        if line['location']['id'] == jitaStationId:
            if line['buy']:
                buy_prices.append(line['price'])
            else:
                sell_prices.append(line['price'])

    # enrich item list with price data
    item['max_buy_price'] = max(buy_prices) if len(buy_prices) else None
    item['min_buy_price'] = min(buy_prices) if len(buy_prices) else None
    item['max_sell_price'] = max(sell_prices) if len(sell_prices) else None
    item['min_sell_price'] = min(sell_prices) if len(sell_prices) else None
    item['buy_prices'] = buy_prices
    item['sell_prices'] = sell_prices
    item['corp_buy'] = None
    if item['max_buy_price'] is not None:
        item['corp_buy'] = (item['max_buy_price'] * 0.95)
    item['corp_buy_total'] = None
    if item['corp_buy'] is not None:
        item['corp_buy_total'] = (item['corp_buy'] * item['amount'])


def getJsonData(endpoint_url):
    # get all Jita offers
    headers = {
        # Eve Api Token is secret, sorry
        'Authorisation': local_settings.ApiToken
    }
    # get all orders from Forge region
    api_response = requests.get(endpoint_url, headers=headers)
    if api_response.status_code > 299:
        raise IOError(endpoint_url + " " + str(api_response.status_code) + " " + pprint.pformat(api_response.text))
    data = api_response.json()
    return data


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