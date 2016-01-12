"""
Survey view
"""
import uuid

from . import TemplatedView
from app.models.quiz_attempt import QuizAttempt


class SurveyBaseView(TemplatedView):
    """ Survey base that other survey types inherit from """
    template = ''

    def get(self, **context):
        """ GET """
        user_id = self.request.GET.get('userId', int(uuid.uuid4().int % 100000000))  # FIXME plz
        attempt = QuizAttempt.get_by_user_id(user_id, context['quiz_type'])
        if not attempt:
            # Start up a new QuizAttempt!
            QuizAttempt.create(user_id=int(user_id), quiz_type=context['quiz_type'])

        context['user_id'] = user_id
        context['questions'] = None  # Eventually maybe this can be server-side-generated React?
        # https://github.com/markfinger/python-react ?
        print context
        self.render_response(self.template, **context)


class SurveyView(SurveyBaseView):
    """ Full survey """
    def get(self):
        self.template = "survey.html"
        context = {
            'request_path': '/survey/',
            'quiz_type': 'fullform'
        }
        super(SurveyView, self).get(**context)


class SurveyShortAView(SurveyBaseView):
    """ Short form A survey """
    def get(self):
        self.template = "survey.html"
        context = {
            'request_path': '/survey/a/',
            'quiz_type': 'short_a'
        }
        super(SurveyShortAView, self).get(**context)


class SurveyShortBView(SurveyBaseView):
    """ Short form B survey """
    def get(self):
        self.template = "survey.html"
        context = {
            'request_path': '/survey/b/',
            'quiz_type': 'short_b'
        }
        super(SurveyShortBView, self).get(**context)
