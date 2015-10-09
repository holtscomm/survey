"""
Survey view
"""
import uuid

from . import TemplatedView
from app.models.quiz_attempt import QuizAttempt


class SurveyView(TemplatedView):
    """ Survey index """

    def get(self):
        """ GET """
        user_id = self.request.GET.get('userId', int(uuid.uuid4().int % 100000000))  # FIXME plz
        attempt = QuizAttempt.get_by_user_id(user_id)
        if not attempt:
            # For now, make a new QuizAttempt for user 1 just for testing.
            QuizAttempt(user_id=user_id).put()

        context = {
            'user_id': user_id,
            'questions': None  # Eventually maybe this can be server-side-generated React?
            # https://github.com/markfinger/python-react ?
        }

        self.render_response("survey.html", **context)
