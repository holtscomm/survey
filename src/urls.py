"""
urls
"""

from webapp2 import Route, SimpleRoute

ROUTES = [
    Route('/', handler='app.views.main.MainView'),
    Route('/survey', handler='app.views.survey.IndexView'),
]
