"""
settings.py Documentation
"""
import os

from settings_secret import SENDGRID_API_KEY, CLIENT_CONFIG

STATIC_VERSION_NUMBER = 1

def is_devappserver():
    return os.environ.get('GAE_APPLICATION') == 'local'

APP_URL = 'localhost:8080' if is_devappserver() else 'https://survey.holtscomm.ca'

OAUTH_CLIENT_ID = '1043482459855-urcbqq64nrha9l4qfqdij1qdh4vlgj77.apps.googleusercontent.com'