from bottle import *
from plugin.bottleCBV import BottleView

# import common_settings
# import local_settings


class BaseController(BottleView):
    """
        Contract parser
    """
    decorators = []
    DEFAULT_ROUTES = ["get", "put", "post", "delete", "index", "options"]
    base_route = None
    route_prefix = None
    view_identifier = "controller"

    # TODO: make messages nice objects
    messages = []
    result = None
    input_data = None
    # TODO: Implement logging type API
    output = ''

    template = ''
    title = ''
    sub_title = ''
    # @TODO: refactor to use array
    js = ''

    def index(self):
        """
        just render the page without any inputs
        :return: 
        """
        return self.__render()

    def __render(self):
        """
            reformat class variables into the response array
            :return: 
        """
        return template(
            self.template,
            page={
                # page title/subtitle
                'title': self.title,
                'sub_title': self.sub_title,
                # page javascript
                'js': self.js,
                # messages to display on top
                'messages': self.messages,
                # form data to preset form for debugging
                'input_data': self.input_data,
                # result for display
                'result': self.result,
                # debug output
                'output': self.output
            }
        )
