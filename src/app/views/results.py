""" Results views """

from . import TemplatedView
from app.models.quiz_attempt import QuizAttempt


class IndexView(TemplatedView):
    """ Survey index """

    def get(self):
        """ GET """
        context = {
            'quiz_attempts': QuizAttempt.get_by_user_id(1)
        }

        self.render_response("results.html", **context)
