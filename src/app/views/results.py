""" Results views """
from app.models.user import User
from . import TemplatedView
from app.models.quiz_attempt import QuizAttempt


class IndexView(TemplatedView):
    """ Survey index """

    def get(self):
        """ GET """
        user_id = self.request.GET.get('userId', 1)
        user = User.get_by_user_id(user_id)

        context = {
            'user': user,
            'quiz_attempts': QuizAttempt.get_all_attempts_for_user_id(user_id)
        }

        self.render_response("results.html", **context)
