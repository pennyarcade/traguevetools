
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route

@route('/')
def hello_world():
    return 'Hello from Bottle!'

@route('/csv/jitaores')
def hello_world():
    output = ''

    output += 'csv / jita ores'

    return output



application = default_app()

