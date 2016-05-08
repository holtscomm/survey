"""
Survey view
"""
from app.models.user import User
from . import TemplatedView
from app.models.quiz_attempt import QuizAttempt


class SurveyBaseView(TemplatedView):
    """ Survey base that other survey types inherit from """
    def get(self, **context):
        """ GET """
        user = User.get_or_create_by_user_id(self.request.GET.get('userId'))
        attempt = QuizAttempt.get_by_user_id(user.user_id, context['quiz_type'])
        if not attempt:
            # Start up a new QuizAttempt!
            QuizAttempt.create(user_id=user.user_id, quiz_type=context['quiz_type'])

        context.update({
            'user': user,
            'user_id': user.user_id,
            'quiz_attempt': attempt
        })

        print context
        self.render_response('survey.html', **context)


class SurveyFullformView(SurveyBaseView):
    """ Full survey """
    def get(self):
        context = {
            'request_path': '/gifts/',
            'quiz_type': 'fullform'
        }
        super(SurveyFullformView, self).get(**context)


class SurveyShortAView(SurveyBaseView):
    """ Short form A survey """
    def get(self):
        context = {
            'request_path': '/gifts/a/',
            'quiz_type': 'short_a'
        }
        super(SurveyShortAView, self).get(**context)


class SurveyShortBView(SurveyBaseView):
    """ Short form B survey """
    def get(self):
        context = {
            'request_path': '/gifts/b/',
            'quiz_type': 'short_b'
        }
        super(SurveyShortBView, self).get(**context)


class SurveyTrialView(SurveyBaseView):
    """ Trial survey """
    def get(self):
        context = {
            'request_path': '/gifts/trial/',
            'quiz_type': 'trial'
        }
        super(SurveyTrialView, self).get(**context)
