import pprint
from dateutil import parser

from base_controller import BaseController

import common_settings
import local_settings
from model import Model
from business_objects.bitbucket_issues import Bitbucket


class DonationsController(BaseController):
    """
        Contract parser
    """
    template = 'donations.html.tpl'
    title = 'Donations'
    sub_title = 'for hosting costs and development'
    js = [
        "/static/node_modules/gentelella/vendors/datatables.net/js/jquery.dataTables.min.js",
        "/static/node_modules/gentelella/vendors/datatables.net-bs/js/dataTables.bootstrap.min.js",
        "/static/node_modules/gentelella/vendors/datatables.net-buttons/js/dataTables.buttons.min.js",
        "/static/node_modules/gentelella/vendors/datatables.net-buttons-bs/js/buttons.bootstrap.min.js",
        "/static/node_modules/gentelella/vendors/datatables.net-buttons/js/buttons.flash.min.js",
        "/static/node_modules/gentelella/vendors/datatables.net-buttons/js/buttons.html5.min.js",
        "/static/node_modules/gentelella/vendors/datatables.net-buttons/js/buttons.print.min.js",
        "/static/node_modules/gentelella/vendors/datatables.net-fixedheader/js/dataTables.fixedHeader.min.js",
        "/static/node_modules/gentelella/vendors/datatables.net-keytable/js/dataTables.keyTable.min.js",
        "/static/node_modules/gentelella/vendors/datatables.net-responsive/js/dataTables.responsive.min.js",
        "/static/node_modules/gentelella/vendors/datatables.net-responsive-bs/js/responsive.bootstrap.js",
        "/static/node_modules/gentelella/vendors/datatables.net-scroller/js/dataTables.scroller.min.js",
        "/static/node_modules/gentelella/vendors/jszip/dist/jszip.min.js",
        "/static/node_modules/gentelella/vendors/pdfmake/build/pdfmake.min.js",
        "/static/node_modules/gentelella/vendors/pdfmake/build/vfs_fonts.js",
        "/static/node_modules/gentelella/vendors/jquery.easy-pie-chart/dist/jquery.easypiechart.min.js",
        '/static/js/donations.js'
    ]
    repo = Bitbucket(
        local_settings.bitbucket_username,
        local_settings.bitbucket_password,
        local_settings.bitbucket_repository
    )

    def index(self):
        """
        just render the page without any inputs
        :return:
        """
        result = {}
        result['journal_table'] = self.__get_wallet_journal()
        result['milestones'] = self.__get_issue_list()
        result['statistics'] = self.__get_statistics(result)

        self.result = result
        self.output = pprint.pformat(self.result)

        return self._render()

    def __get_wallet_journal(self):
        """
        get wallet journal entries
        :return:
        """
        query = Model.WalletTransactions.select()
        self.log.info(pprint.pformat(query))
        journal_table = []

        for row in query:
            journal_table.append(
                Model.get_dictionary_from_model(row)
            )

        return journal_table

    def __get_issue_list(self):
        """
        Get all issues for overview
        :return:
        """
        success, issues = self.repo.issue.all()
        result = {}
        tally = 0

        if success:
            for index, issue in enumerate(issues['issues']):
                issue['reported_by'] = {
                    u'avatar': u'',
                    u'display_name': u'Anonymous',
                    u'first_name': u'',
                    u'is_staff': False,
                    u'is_team': False,
                    u'last_name': u'Anonymous',
                    u'resource_uri': u'',
                    u'username': u'anonymous'
                }
                issue['created_on'] = parser.parse(issue['created_on'])
                issue['utc_created_on'] = parser.parse(issue['utc_created_on'])
                issue['utc_last_updated'] = parser.parse(issue['utc_last_updated'])

                parts = issue['content'].split('----', 1)
                if len(parts) > 1:
                    issue['content'] = parts[1]
                    for line in parts[0].splitlines():
                        lparts = line.split(":", 1)
                        if len(lparts) > 1:
                            if lparts[0].strip() in ['avatar', 'display_name']:
                                issue['reported_by'][lparts[0].strip()] = lparts[1].strip()
                            else:
                                issue[lparts[0].strip()] = lparts[1].strip()

                milestone = issue['metadata']['milestone']
                amount = issue['donation_amount'] if 'donation_amount' in issue else 0

                if milestone in result.keys():
                    result[milestone]['issues'].append(issue)
                    result[milestone]['amount'] += int(amount)
                    tally += int(amount)
                elif milestone is None:
                    pass
                else:
                    result[milestone] = {
                        'issues': [
                            issue
                        ],
                        'amount': int(amount),
                        'tally': tally
                    }
                    tally += int(amount)

            return result
        else:
            self.messages.append(
                {
                    'type': 'danger',
                    'dismissible': False,
                    'content': '<strong>Error:</strong> Unable to fetch Issues:<pre>' + issues + '</pre>'
                }
            )

    def __get_statistics(self, result):
        """
        Calculate some statistics

        :return:
        """
        result = {}
        result['hosting_costs'] = 3780000000
        result['total_donations'] = 0

        query = Model.WalletTransactions.select().order_by(
            Model.WalletTransactions.date.desc()
        )

        for row in query:
            result['total_donations'] += Model.get_dictionary_from_model(row)['amount']

        result['percentage'] = result['total_donations'] / result['hosting_costs'] * 100

        return result