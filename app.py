from evetools import app
import local_config as config

if __name__ == '__main__':
    app.run(
        port=config.PORT,
        host=config.HOST,
        debug=True,
        ssl_context='adhoc'
    )
