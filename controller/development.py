from dateutil import parser

from bottle import request
from plugin.bottleCBV import route

# import common_settings
import local_settings
from base_controller import BaseController

from bitbucket.bitbucket import Bitbucket


class DevelopmentController(BaseController):
    """
    Development page
    """
    template = 'development.html.tpl'
    title = 'Development'
    sub_title = 'Bugs & Features'
    js = '/static/js/development.js'
    repo = Bitbucket(
        local_settings.bitbucket_username,
        local_settings.bitbucket_password,
        local_settings.bitbucket_repository
    )
    content = """display_name: %s        
----
%s
"""

    def index(self):
        """
        just render the page without any inputs
        :return: 
        """
        self.__get_issue_list()
        return self._render()

    def post(self):
        """
        Process forms
        """
        # Todo: Verify form data
        if request.forms.get('form') == "new_issue":
            self.__new_issue()
        else:
            self.messages.append(
                {
                    'type': 'danger',
                    'dismissible': False,
                    'content': '<strong>Error:</strong> Invalid form data'
                }
            )

        self.__get_issue_list()
        return self._render()

    def get(self, issue_id):
        """
        get issue details
        :param issue_id: 
        :return: 
        """
        self.__get_issue_list()
        self.__get_issue_details(issue_id)
        return self._render()

    @route('/development/<issue_id:int>/', method='POST')
    def post_id(self, issue_id):
        """
        add comment to issue
        :param issue_id: 
        :return: 
        """
        # Todo: Verify form data
        if request.forms.get('form') == "new_issue":
            self.__new_issue()
        elif request.forms.get('form') == "reply_issue":
            self.__comment(issue_id)
        else:
            self.messages.append(
                {
                    'type': 'danger',
                    'dismissible': False,
                    'content': '<strong>Error:</strong> Invalid form data'
                }
            )

        self.__get_issue_list()
        self.__get_issue_details(issue_id)
        return self._render()

    def __comment(self, issue_id):
        content = self.content % (
            request.forms.get('reply_name'),
            request.forms.get('reply_content'))
        self.repo.issue.comment.create(
            issue_id,
            content=content
        )

    def __new_issue(self):
        content = self.content % (
            request.forms.get('issue_name'),
            request.forms.get('issue_content')
        )
        self.repo.issue.create(
            title=request.forms.get('issue_subject'),
            content=content,
            component=request.forms.get('issue_component'),
            status='new',
            kind=request.forms.get('issue_kind'),
            priority=request.forms.get('issue_priority')
        )

    def __get_issue_list(self):
        """
        Get all issues for overview
        :return: 
        """
        if self.result is None:
            self.result = dict()

        success, issues = self.repo.issue.all()
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
                            issue['reported_by'][lparts[0].strip()] = lparts[1].strip()

            self.result['issues'] = issues
        else:
            self.messages.append(
                {
                    'type': 'danger',
                    'dismissible': False,
                    'content': '<strong>Error:</strong> Unable to fetch Issues:<pre>' + issues + '</pre>'
                }
            )

    def __get_issue_details(self, issue_id):
        """
        Get issue details
        :param issue_id: 
        :return: 
        """
        if self.result is None:
            self.result = dict()

        success, issue = self.repo.issue.get(issue_id)
        if success:
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
                        issue['reported_by'][lparts[0].strip()] = lparts[1].strip()

            self.result['current'] = issue

            success, comments = self.repo.issue.comment.all(issue_id)
            if success:

                for index, comment in enumerate(comments):
                    comment['author_info'] = {
                        u'avatar': u'',
                        u'display_name': u'Anonymous',
                        u'first_name': u'',
                        u'is_staff': False,
                        u'is_team': False,
                        u'last_name': u'Anonymous',
                        u'resource_uri': u'',
                        u'username': u'anonymous'
                    }
                    comment['utc_created_on'] = parser.parse(comment['utc_created_on'])
                    comment['utc_updated_on'] = parser.parse(comment['utc_updated_on'])

                    parts = comment['content'].split('----', 1)
                    if len(parts) > 1:
                        comment['content'] = parts[1]
                        for line in parts[0].splitlines():
                            lparts = line.split(":", 1)
                            if len(lparts) > 1:
                                comment['author_info'][lparts[0].strip()] = lparts[1].strip()

                self.result['current']['comments'] = comments

            else:
                self.messages.append(
                    {
                        'type': 'danger',
                        'dismissible': False,
                        'content': '<strong>Error:</strong> Unable to fetch comments for Issue #' + issue_id + ':<pre>' + comments + '</pre>'
                    }
                )

        else:
            self.messages.append(
                {
                    'type': 'danger',
                    'dismissible': False,
                    'content': '<strong>Error:</strong> Unable to fetch Issue #' + issue_id + ':<pre>' + issue + '</pre>'
                }
            )
