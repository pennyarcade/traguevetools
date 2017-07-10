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

import local_settings
import common_settings
from model import Model


logging.basicConfig(
    filename='../../logs/getTreasurerWallet.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)
Model.db.connect()

logger = logging.getLogger('peewee')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.FileHandler('../../logs/peewee.log'))

# Constant definitions
refresh_url = 'https://login.eveonline.com/oauth/token'
headers = {
    # always keep ur secret data in a separate config file that is ignored in your vcs
    'Authorization': 'Basic ' + base64.b64encode(
        local_settings.eve_oauth_client_id + ':' + local_settings.eve_oauth_secret_key
    ),
    'User-Agent': local_settings.eve_oauth_client_name
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
    session.headers.update({'UserAgent': local_settings.eve_oauth_client_name})

    # Get authorization (refresh token)
    r = requests.post('https://login.eveonline.com/oauth/token', params=query, headers=headers)
    response = r.json()
    print(r.text)
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

    wallet_result = wallet_journal.json()
    if 'error' not in wallet_result:
        for row in wallet_result:
            logging.info('Building item \n{}'.format(pformat(row)))
            item, created = Model.WalletTransactions.get_or_create(
                amount=row[u'amount'] if u'amount' in row else None,
                argumentName=row[u'argument_name'] if u'argument_name' in row else None,
                argumentValue=row[u'argument_value'] if u'argument_value' in row else None,
                balance=row[u'balance'] if u'balance' in row else None,
                date=row[u'date'],
                firstPartyID=row[u'first_party_id'] if u'first_party_id' in row else None,
                firstPartyType=row[u'first_party_type'] if u'first_party_type' in row else None,
                reason=row[u'reason'] if u'reason' in row else None,
                refID=row[u'ref_id'],
                refTypeID=row[u'ref_type_id'],
                secondPartyID=row[u'second_party_id'] if u'second_party_id' in row else None,
                secondPartyType=row[u'second_party_type'] if u'second_party_type' in row else None,
                taxAmount=row[u'tax_amount'] if u'tax_amount' in row else None,
                taxRecieverID=row[u'tax_reciever_id'] if u'tax_reciever_id' in row else None,
            )
            if created:
                logging.info('Item #{} already created.'.format(row[u'ref_id']))
            else:
                logging.info('Inserting item #{}'.format(row[u'ref_id']))
            item.save()
    else:
        logging.error(
            'Response headers \n{}'.format(
                pformat(wallet_result)
            )
        )

# if called from command line run main function
if __name__ == '__main__':
    run()
