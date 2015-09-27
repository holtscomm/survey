"""
urls
"""

from webapp2 import Route

ROUTES = [
    Route('/', handler='app.views.main.MainView'),
    Route('/survey/<page_num:\d+>', handler='app.views.survey.SurveyView'),
    Route('/results', handler='app.views.results.IndexView'),
    Route('/api/v1/survey/<user_id:\d+>/<page_num:\d+>', handler='app.views.api.v1.survey.SurveyPageApiHandler')
]
