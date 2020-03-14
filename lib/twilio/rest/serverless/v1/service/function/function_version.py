# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class FunctionVersionList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, service_sid, function_sid):
        """
        Initialize the FunctionVersionList

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the Service that the Function Version resource is associated with
        :param function_sid: The SID of the function that is the parent of the function version

        :returns: twilio.rest.serverless.v1.service.function.function_version.FunctionVersionList
        :rtype: twilio.rest.serverless.v1.service.function.function_version.FunctionVersionList
        """
        super(FunctionVersionList, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, 'function_sid': function_sid, }
        self._uri = '/Services/{service_sid}/Functions/{function_sid}/Versions'.format(**self._solution)

    def stream(self, limit=None, page_size=None):
        """
        Streams FunctionVersionInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.serverless.v1.service.function.function_version.FunctionVersionInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists FunctionVersionInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.serverless.v1.service.function.function_version.FunctionVersionInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of FunctionVersionInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of FunctionVersionInstance
        :rtype: twilio.rest.serverless.v1.service.function.function_version.FunctionVersionPage
        """
        data = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(method='GET', uri=self._uri, params=data, )

        return FunctionVersionPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of FunctionVersionInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of FunctionVersionInstance
        :rtype: twilio.rest.serverless.v1.service.function.function_version.FunctionVersionPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return FunctionVersionPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a FunctionVersionContext

        :param sid: The SID that identifies the Function Version resource to fetch

        :returns: twilio.rest.serverless.v1.service.function.function_version.FunctionVersionContext
        :rtype: twilio.rest.serverless.v1.service.function.function_version.FunctionVersionContext
        """
        return FunctionVersionContext(
            self._version,
            service_sid=self._solution['service_sid'],
            function_sid=self._solution['function_sid'],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a FunctionVersionContext

        :param sid: The SID that identifies the Function Version resource to fetch

        :returns: twilio.rest.serverless.v1.service.function.function_version.FunctionVersionContext
        :rtype: twilio.rest.serverless.v1.service.function.function_version.FunctionVersionContext
        """
        return FunctionVersionContext(
            self._version,
            service_sid=self._solution['service_sid'],
            function_sid=self._solution['function_sid'],
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Serverless.V1.FunctionVersionList>'


class FunctionVersionPage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the FunctionVersionPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param service_sid: The SID of the Service that the Function Version resource is associated with
        :param function_sid: The SID of the function that is the parent of the function version

        :returns: twilio.rest.serverless.v1.service.function.function_version.FunctionVersionPage
        :rtype: twilio.rest.serverless.v1.service.function.function_version.FunctionVersionPage
        """
        super(FunctionVersionPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of FunctionVersionInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.serverless.v1.service.function.function_version.FunctionVersionInstance
        :rtype: twilio.rest.serverless.v1.service.function.function_version.FunctionVersionInstance
        """
        return FunctionVersionInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            function_sid=self._solution['function_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Serverless.V1.FunctionVersionPage>'


class FunctionVersionContext(InstanceContext):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, service_sid, function_sid, sid):
        """
        Initialize the FunctionVersionContext

        :param Version version: Version that contains the resource
        :param service_sid: The SID of the Service to fetch the Function Version resource from
        :param function_sid: The SID of the function that is the parent of the Function Version resource to fetch
        :param sid: The SID that identifies the Function Version resource to fetch

        :returns: twilio.rest.serverless.v1.service.function.function_version.FunctionVersionContext
        :rtype: twilio.rest.serverless.v1.service.function.function_version.FunctionVersionContext
        """
        super(FunctionVersionContext, self).__init__(version)

        # Path Solution
        self._solution = {'service_sid': service_sid, 'function_sid': function_sid, 'sid': sid, }
        self._uri = '/Services/{service_sid}/Functions/{function_sid}/Versions/{sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch the FunctionVersionInstance

        :returns: The fetched FunctionVersionInstance
        :rtype: twilio.rest.serverless.v1.service.function.function_version.FunctionVersionInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return FunctionVersionInstance(
            self._version,
            payload,
            service_sid=self._solution['service_sid'],
            function_sid=self._solution['function_sid'],
            sid=self._solution['sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Serverless.V1.FunctionVersionContext {}>'.format(context)


class FunctionVersionInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    class Visibility(object):
        PUBLIC = "public"
        PRIVATE = "private"
        PROTECTED = "protected"

    def __init__(self, version, payload, service_sid, function_sid, sid=None):
        """
        Initialize the FunctionVersionInstance

        :returns: twilio.rest.serverless.v1.service.function.function_version.FunctionVersionInstance
        :rtype: twilio.rest.serverless.v1.service.function.function_version.FunctionVersionInstance
        """
        super(FunctionVersionInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'service_sid': payload.get('service_sid'),
            'function_sid': payload.get('function_sid'),
            'path': payload.get('path'),
            'visibility': payload.get('visibility'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'url': payload.get('url'),
        }

        # Context
        self._context = None
        self._solution = {
            'service_sid': service_sid,
            'function_sid': function_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: FunctionVersionContext for this FunctionVersionInstance
        :rtype: twilio.rest.serverless.v1.service.function.function_version.FunctionVersionContext
        """
        if self._context is None:
            self._context = FunctionVersionContext(
                self._version,
                service_sid=self._solution['service_sid'],
                function_sid=self._solution['function_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: The unique string that identifies the Function Version resource
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def account_sid(self):
        """
        :returns: The SID of the Account that created the Function Version resource
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def service_sid(self):
        """
        :returns: The SID of the Service that the Function Version resource is associated with
        :rtype: unicode
        """
        return self._properties['service_sid']

    @property
    def function_sid(self):
        """
        :returns: The SID of the function that is the parent of the function version
        :rtype: unicode
        """
        return self._properties['function_sid']

    @property
    def path(self):
        """
        :returns: The URL-friendly string by which the function version can be referenced
        :rtype: unicode
        """
        return self._properties['path']

    @property
    def visibility(self):
        """
        :returns: The access control that determines how the function version can be accessed
        :rtype: FunctionVersionInstance.Visibility
        """
        return self._properties['visibility']

    @property
    def date_created(self):
        """
        :returns: The ISO 8601 date and time in GMT when the Function Version resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def url(self):
        """
        :returns: The absolute URL of the Function Version resource
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch the FunctionVersionInstance

        :returns: The fetched FunctionVersionInstance
        :rtype: twilio.rest.serverless.v1.service.function.function_version.FunctionVersionInstance
        """
        return self._proxy.fetch()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Serverless.V1.FunctionVersionInstance {}>'.format(context)
