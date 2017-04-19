import sys
from bitbucket.bitbucket import Bitbucket
import local_settings

class BitbucketException(Exception):
    """
        Bitbucket lookup errors
    """
    def __init__(self, message):
        self.traceback = sys.exc_info()
        super(BitbucketException, self).__init__(message)

class IssueCollection:
    """
        Collection of Issues
    """
    bb = None

    count = None
    filter = None
    issues = list()
    search = None

    def __init__(self):
        """
            Setup bitbucket repository
        """
        try:
            self.bb = Bitbucket(
                local_settings.bitbucket_username,
                local_settings.bitbucket_password,
                local_settings.bitbucket_repository
            )
        except BaseException as e:
            raise BitbucketException(
                e
            )

        data = self.get_all()

        self.count = data['count']
        self.filter = data['filter']
        for item in data['issues']:
            self.issues.append(
                Issue(
                    self.bb,
                    from_dict=item
                )
            )
        self.search = data['search']

    def get_all(self):
        """
        get all issues
        
        :return: 
        """
        success, result = self.bb.issues.all()

        if not success:
            raise BitbucketException(
                'Error getting Issues'
            )

        return result


class Issue:
    """
        Representation of a Bitbucket Issue
    """
    bb = None

    created_on = None
    utc_created_on = None
    utc_last_updated = None

    comment_count = None
    follower_count = None

    local_id = None
    resource_uri = None
    title = None
    content = None
    comments = None

    is_spam = None

    component = None
    kind = None
    milestone = None
    version = None
    priority = None
    status = None

    reported_by = None
    responsible = None

    def __init__(self, bb, **kwargs):
        """
        :param bb: instance of Bitbucket
        :param kwargs: 
        """
        # if id given fetch from repository
        # if url given fetch from url
        # if dict given build from dictionary
        # check all parameters
        pass

    def __from_dict(self, data):
        """
        create issue from dictionary of values as returned by API
        
        :param data: 
        :return: 
        """
        for key, value in data:
            if key == 'metadata':
                for metakey, metavalue in value:
                    setattr(self, metakey, metavalue)
            else:
                setattr(self, key, value)

    def __from_id(self, id):
        """
        fetch issue by ID
        :param id: 
        :return: 
        """
        success, result = self.bb.get(id)

        if not success:
            raise BitbucketException(
                'Error getting Issue %d' % id
            )

        self.__from_dict(result)

    def save(self):
        """
        create / update issue
        
        :return: 
        """

        if self.local_id is not None:
            try:
                success, result = self.bb.update(
                    self.local_id,
                    title=self.title,
                    content=self.content,
                    component=self.component,
                    milestone=self.milestone,
                    version=self.version,
                    responsible=self.responsible['username'] if self.responsible else None,
                    status=self.status,
                    kind=self.kind
                )
            except Exception as e:
                raise BitbucketException(
                    'Error updating issue %d' % self.local_id,
                )

            if not success:
                try:
                    success, result = self.bb.create(
                        self.local_id,
                        title=self.title,
                        content=self.content,
                        component=self.component,
                        milestone=self.milestone,
                        version=self.version,
                        responsible=self.responsible['username'] if self.responsible else None,
                        status=self.status,
                        kind=self.kind
                    )
