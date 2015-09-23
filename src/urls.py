"""
urls
"""

from webapp2 import Route

ROUTES = [
    Route('/', handler='app.views.main.MainView'),
    Route('/survey/<page_num:\d+>', handler='app.views.survey.SurveyView'),
    Route('/results', handler='app.views.results.IndexView'),
]
