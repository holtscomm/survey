"""
urls
"""

from webapp2 import Route

ROUTES = [
    Route('/', handler='app.views.main.MainView'),
    Route('/gifts/', handler='app.views.survey.SurveyFullformView'),
    Route('/gifts/a/', handler='app.views.survey.SurveyShortAView'),
    Route('/gifts/b/', handler='app.views.survey.SurveyShortBView'),
    Route('/gifts/trial/', handler='app.views.survey.SurveyTrialView'),
    Route('/results/', handler='app.views.results.IndexView'),
    Route('/api/v1/survey/<user_id:.+>/<page_num:\d+>/', handler='app.views.api.v1.survey.SurveyPageApiHandler'),
    Route('/api/v1/survey/getFirstPage/', handler='app.views.api.v1.survey.SurveyGetFirstPageApiHandler'),
    Route('/api/v1/survey/post/<user_id:.+>/', handler='app.views.api.v1.survey.SurveyPageApiHandler'),
]
