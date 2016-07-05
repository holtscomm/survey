""" superadmin.py """
from google.appengine.ext import ndb

from app.models.quiz_attempt import QuizAttempt
from app.models.user import User
from app.views import TemplatedView

class MainView(TemplatedView):
    @ndb.synctasklet
    def get_superadmin_index_data(self):
        paid_survey_users, all_quiz_attempts = yield (
            User.get_paid_survey_users().fetch_async(),
            QuizAttempt.get_all_attempts().fetch_async()
        )
        all_users = yield ndb.get_multi_async([User.build_key(attempt.user_id) for attempt in all_quiz_attempts])
        raise ndb.Return((paid_survey_users, all_quiz_attempts, all_users))

    def get(self):
        paid_survey_users, all_quiz_attempts, all_users = self.get_superadmin_index_data()

        context = {
            'paid_survey_users': len(paid_survey_users),
            # 'paid_survey_users_last_30_days': len(User.get_paid_survey_users_last_30_days().fetch())
            'quiz_attempt_data': all_quiz_attempts,
            'all_users': all_users
        }

        self.render_response('superadmin/index.html', **context)


class GenerateView(TemplatedView):
    def get(self):
        self.render_response('superadmin/generate.html')
