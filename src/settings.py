"""
settings.py Documentation
"""
import os

from settings_secret import SENDGRID_API_KEY

STATIC_VERSION_NUMBER = 1

def is_devappserver():
    return True if os.environ['APPLICATION_ID'].startswith('dev') else False


APP_URL = 'localhost:8079' if is_devappserver() else 'https://survey.holtscomm.ca'
