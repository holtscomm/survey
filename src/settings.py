"""
settings.py Documentation
"""
import os

from settings_secret import SENDGRID_API_KEY

STATIC_VERSION_NUMBER = 1

APP_URL = 'localhost:8079' # if is_devappserver() else 'https://survey.holtscomm.ca'
