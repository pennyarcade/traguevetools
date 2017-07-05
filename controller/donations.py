import StringIO
import pprint
import requests
import traceback

from bottle import template, request
from base_controller import BaseController

import common_settings
import local_settings
from model import Model


class DonationsController(BaseController):
    """
        Contract parser
    """
    template = 'donations.html.tpl'
    title = 'Donations'
    sub_title = 'for hosting costs and development'
    js = '/static/js/donations.js'
    result = []

    def index(self):
        """
        just render the page without any inputs
        :return:
        """
        self.__get_wallet_journal()
        return self._render()

    def __get_wallet_journal(self):
        """
        get wallet journal entries
        :return:
        """
        result = Model.WalletTransactions.select()
        self.log.info(pprint.pformat(result))
        pprint.pprint(result)
        for row in result:
            result.append(
                Model.get_dictionary_from_model(row)
            )

            self.output += pprint.pformat(
                Model.get_dictionary_from_model(row)
            )
            self.output += '\n\n'

