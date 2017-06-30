"""
    example script to demonstrate usage of refresh token in cron
"""
# my config file is in the directory above so I need to make that available
import sys
sys.path.append("..")

# Imports
import logging
import base64

import requests
from requests.sessions import Session
from pprint import pprint, pformat

import common_settings


logging.basicConfig(filename='logs/getTreasurerWallet.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')

# Constant definitions
refresh_url = 'https://login.eveonline.com/oauth/token'
headers = {
    # always keep ur secret data in a separate config file that is ignored in your vcs
    'Authorization': 'Basic ' + base64.b64encode(
        common_settings.client_id + ':' + common_settings.client_secret
    ),
    'User-Agent': common_settings.client_name
}
query = {
    'grant_type': 'refresh_token',
    'refresh_token': common_settings.refresh_token
}
wallet_endpiont = 'https://esi.tech.ccp.is/latest/characters/{0}/wallets/journal/?datasource=tranquility'


def run():
    """
    Capsule main routine in function to make the script importable if needed
    :return:
    """

    session = Session()
    session.headers.update({'UserAgent': common_settings.client_name})

    # Get authorization (refresh token)
    r = requests.post('https://login.eveonline.com/oauth/token', params=query, headers=headers)
    response = r.json()
    access_token = response['access_token']
    logging.warn("Access Token {}".format(access_token))
    session.headers.update({'Authorization': 'Bearer ' + access_token})

    logging.info('Getting wallet journal from {}'.format(
        wallet_endpiont.format(
            common_settings.treasurer_character_id
        )
    ))
    wallet_journal = session.get(
        wallet_endpiont.format(
            common_settings.treasurer_character_id
        )
    )
    logging.info('Response status {}'.format(wallet_journal.status_code))
    logging.info('Response headers \n{}'.format(pformat(wallet_journal.headers)))

    # just dump to commandline for demonstration purpose
    pprint(wallet_journal.json())


# if called from command line run main function
if __name__ == '__main__':
    run()
