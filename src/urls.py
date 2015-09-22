"""
urls
"""

from webapp2 import Route

ROUTES = [
    Route('/', handler='app.views.main.MainView'),
    Route('/survey', handler='app.views.survey.IndexView'),
    Route('/results', handler='app.views.results.IndexView'),
]
