
from bottle import default_app, route
import requests
import traceback
import pprint


@route('/')
def hello_world():
    return 'Hello from Bottle!'

@route('/csv/jitaores')
def hello_world():
    output = ''
    output += 'csv / jita ores'

    return output



application = default_app()

