import StringIO
import pprint
import traceback
from dateutil import parser

import common_settings
import local_settings

from model import Model
from bitbucket.bitbucket import Bitbucket

def development(request= None, response=None, issue_id=None):
    """
    :param request: 
    :return: 
    """
    # saves debug output
    output = ''
    # saves messages to the user
    messages = []
    # result for display
    result = {}
    # form data to preset form for debugging
    inputdata = None

    repo = Bitbucket(
        local_settings.bitbucket_username,
        local_settings.bitbucket_password,
        local_settings.bitbucket_repository
    )

    if request.method == 'POST':
        # output += pprint.pformat(request.forms.allitems())

        # Todo: Verify form data

        content = """display_name: %s        
----
%s
"""
        if request.forms.get('form') == "new_issue":
            content = content % (request.forms.get('issue_name'), request.forms.get('issue_content'))
            repo.issue.create(
                title=request.forms.get('issue_subject'),
                content=content,
                component=request.forms.get('issue_component'),
                status='new',
                kind=request.forms.get('issue_kind'),
                priority=request.forms.get('issue_priority')
            )
        elif request.forms.get('form') == "reply_issue":
            content = content % (request.forms.get('reply_name'), request.forms.get('reply_content'))
            repo.issue.comment.create(
                issue_id,
                content=content
            )
        else:
            messages.append(
                {
                    'type': 'danger',
                    'dismissible': False,
                    'content': '<strong>Error:</strong> Invalid form data'
                }
            )

    success, issues = repo.issue.all()
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


        result['issues'] = issues
    else:
        messages.append(
            {
                'type': 'danger',
                'dismissible': False,
                'content': '<strong>Error:</strong> Unable to fetch Issues:<pre>' + issues + '</pre>'
            }
        )

    if issue_id:
        success, issue = repo.issue.get(issue_id)
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

            result['current'] = issue

            success, comments = repo.issue.comment.all(issue_id)
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

                result['current']['comments'] = comments

            else:
                messages.append(
                    {
                        'type': 'danger',
                        'dismissible': False,
                        'content': '<strong>Error:</strong> Unable to fetch comments for Issue #' + issue_id + ':<pre>' + comments + '</pre>'
                    }
                )

        else:
            messages.append(
                {
                    'type': 'danger',
                    'dismissible': False,
                    'content': '<strong>Error:</strong> Unable to fetch Issue #' + issue_id + ':<pre>' + issues + '</pre>'
                }
            )


    #output += pprint.pformat(request.method)
    #output += pprint.pformat(request.url)

    return dict(
        # messages & notifications
        messages=messages,
        # result for display
        result=result,
        # form data to preset form for debugging
        inputdata=inputdata,
        # debug output
        output=output + ' Hola!'
    )
