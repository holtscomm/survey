""" Results views """
from google.appengine.ext import ndb

from app.models.user import User
from . import TemplatedView
from app.models.quiz_attempt import QuizAttempt


class IndexView(TemplatedView):
    """ Survey index """
    @ndb.synctasklet
    def get_results_data(self, user_id):
        """ Get the results needed for the survey page """
        users, quiz_attempts = yield(
            User.get_by_user_id_async(user_id),
            QuizAttempt.get_all_attempts_for_user_id_async(user_id)
        )
        raise ndb.Return((users, quiz_attempts))

    def get(self):
        """ GET """
        user_id = self.request.GET.get('userId', 1)
        user, quiz_attempts = self.get_results_data(user_id)

        context = {
            'user': user,
            'quiz_attempts': quiz_attempts
        }

        self.render_response("results.html", **context)
