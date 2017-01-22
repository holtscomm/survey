"""
settings.py Documentation
"""
import os

STATIC_VERSION_NUMBER = 1

SENDGRID_API_KEY = '***REMOVED***'


def is_devappserver():
    return True if os.environ['APPLICATION_ID'].startswith('dev') else False


APP_URL = 'localhost:8079' if is_devappserver() else 'http://survey.holtscomm.ca'
