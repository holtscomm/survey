"""
urls
"""

from webapp2_extras.routes import RedirectRoute

from webapp2 import Route

ROUTES = [
    RedirectRoute('/superadmin/', name='superadmin-main', handler='app.views.superadmin.MainView'),
    RedirectRoute('/superadmin/generate/', name='generate-surveys', handler='app.views.superadmin.GenerateView', strict_slash=True),
    RedirectRoute('/superadmin/questions/', name='view-questions', handler='app.views.superadmin.PrintQuestionsView', strict_slash=True),

    Route('/', handler='app.views.main.MainView'),
    RedirectRoute('/gifts/', name='full-gift-survey', handler='app.views.survey.SurveyFullformView', strict_slash=True),
    RedirectRoute('/gifts/a/', name='short-a-gift-survey', handler='app.views.survey.SurveyShortAView', strict_slash=True),
    RedirectRoute('/gifts/b/', name='short-b-gift-survey', handler='app.views.survey.SurveyShortBView', strict_slash=True),
    RedirectRoute('/gifts/trial/', name='trial-gift-survey', handler='app.views.survey.SurveyTrialView', strict_slash=True),
    RedirectRoute('/results/', name='results', handler='app.views.results.IndexView', strict_slash=True),
    Route('/api/v1/survey/<user_id:.+>/<page_num:\d+>/', handler='app.views.api.v1.survey.SurveyPageApiHandler'),
    Route('/api/v1/survey/getFirstPage/', handler='app.views.api.v1.survey.SurveyGetFirstPageApiHandler'),
    Route('/api/v1/survey/post/<user_id:.+>/', handler='app.views.api.v1.survey.SurveyPageApiHandler'),
    Route('/api/v1/survey/purchase/', handler='app.views.api.v1.survey.SurveyPurchaseApiHandler'),
]
