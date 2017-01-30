"""
settings.py Documentation
"""
import os

STATIC_VERSION_NUMBER = 1

SENDGRID_API_KEY = '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'


def is_devappserver():
    return True if os.environ['APPLICATION_ID'].startswith('dev') else False


APP_URL = 'localhost:8079' if is_devappserver() else 'https://survey.holtscomm.ca'
