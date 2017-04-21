import StringIO
import pprint
import traceback

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

    success, issues = repo.issue.all()
    if success:
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
            result['current'] = issue

            success, comments = repo.issue.comment.all(issue_id)
            if success:
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


    output += pprint.pformat(result)

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



