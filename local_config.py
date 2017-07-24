# -*- encoding: utf-8 -*-
import datetime

# -----------------------------------------------------
# Application configurations
# ------------------------------------------------------
DEBUG = True
SECRET_KEY = 'CredulityIsNotAVirtue!'
PORT = 5015
HOST = 'localhost'

# -----------------------------------------------------
# SQL Alchemy configs
# -----------------------------------------------------
SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'

# -----------------------------------------------------
# ESI Configs
# -----------------------------------------------------
ESI_DATASOURCE = 'tranquility'  # Change it to 'singularity' to use the test server
ESI_SWAGGER_JSON = 'https://esi.tech.ccp.is/latest/swagger.json?datasource=%s' % ESI_DATASOURCE
ESI_SECRET_KEY = 'b0c0669249f44014a0b83dc9e578d4f7'  # your secret key
ESI_CLIENT_ID = '4QHREgHrWG5m2NegFB2wtZgVzxHxWrkewvOWEkpo'  # your client ID
ESI_CALLBACK = 'http://%s:%d/authcallback' % (HOST, PORT)  # the callback URI you gave CCP
ESI_USER_AGENT = 'Eve Tools Test'


# ------------------------------------------------------
# Session settings for flask login
# ------------------------------------------------------
PERMANENT_SESSION_LIFETIME = datetime.timedelta(days=30)

# ------------------------------------------------------
# DO NOT EDIT
# Fix warnings from flask-sqlalchemy / others
# ------------------------------------------------------
SQLALCHEMY_TRACK_MODIFICATIONS = True
