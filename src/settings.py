"""
settings.py Documentation
"""
import os

STATIC_VERSION_NUMBER = 1

SENDGRID_API_KEY = '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'


def is_devappserver():
    return True if os.environ['APPLICATION_ID'].startswith('dev') else False


APP_URL = 'localhost:8079' if is_devappserver() else 'http://survey.keithdwalker.ca/'
