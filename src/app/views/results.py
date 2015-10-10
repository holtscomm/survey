""" Results views """

from . import TemplatedView
from app.models.quiz_attempt import QuizAttempt


class IndexView(TemplatedView):
    """ Survey index """

    def get(self):
        """ GET """
        user_id = self.request.GET.get('userId', 1)

        context = {
            'user_id': user_id,
            'quiz_attempt': QuizAttempt.get_by_user_id(user_id)
        }

        self.render_response("results.html", **context)
