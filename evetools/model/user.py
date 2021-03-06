from flask_login import UserMixin
import time
from datetime import datetime

# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
from evetools import evedb


# -----------------------------------------------------------------------
# Database models
# -----------------------------------------------------------------------
class User(evedb.Model, UserMixin):
    # our ID is the character ID from EVE API
    character_id = evedb.Column(
        evedb.BigInteger,
        primary_key=True,
        autoincrement=False
    )
    character_owner_hash = evedb.Column(evedb.String(255))
    character_name = evedb.Column(evedb.String(200))

    # SSO Token stuff
    access_token = evedb.Column(evedb.String(100))
    access_token_expires = evedb.Column(evedb.DateTime())
    refresh_token = evedb.Column(evedb.String(100))

    def get_id(self):
        """ Required for flask-login """
        return self.character_id

    def get_sso_data(self):
        """ Little "helper" function to get formated data for esipy security
        """
        return {
            'access_token': self.access_token,
            'refresh_token': self.refresh_token,
            'expires_in': (
                self.access_token_expires - datetime.utcnow()
            ).total_seconds()
        }

    def update_token(self, token_response):
        """ helper function to update token data from SSO response """
        self.access_token = token_response['access_token']
        self.access_token_expires = datetime.fromtimestamp(
            time.time() + token_response['expires_in'],
        )
        if 'refresh_token' in token_response:
            self.refresh_token = token_response['refresh_token']