""" superadmin.py """
from google.appengine.ext import ndb

import settings
from app.models.question import Question
from app.models.quiz_attempt import QuizAttempt
from app.models.user import User
from app.views import TemplatedView


class MainView(TemplatedView):
    @ndb.synctasklet
    def get_superadmin_index_data(self):
        paid_survey_users, all_quiz_attempts, paid_quiz_attempts = yield (
            User.get_paid_survey_users().fetch_async(),
            QuizAttempt.get_all_attempts().fetch_async(),
            QuizAttempt.get_non_trial_attempts().fetch_async()
        )
        all_users = yield ndb.get_multi_async([User.build_key(attempt.user_id) for attempt in all_quiz_attempts])
        raise ndb.Return((paid_survey_users, all_quiz_attempts, all_users, paid_quiz_attempts))

    def get(self):
        paid_survey_users, all_quiz_attempts, all_users, paid_quiz_attempts = self.get_superadmin_index_data()

        context = {
            'paid_survey_users': len(paid_survey_users),
            # 'paid_survey_users_last_30_days': len(User.get_paid_survey_users_last_30_days().fetch())
            'quiz_attempt_data': all_quiz_attempts,
            'all_users': all_users,
            'paid_quiz_attempts': paid_quiz_attempts,
            'env': 'local' if settings.is_devappserver() else 'not-local'
        }

        self.render_response('superadmin/index.html', **context)


class GenerateView(TemplatedView):
    def get(self):
        self.render_response('superadmin/generate.html')


class PrintQuestionsView(TemplatedView):
    def get(self):
        context = {
            'questions': Question.get_all_questions(ordered=True)
        }

        self.render_response('superadmin/print_questions.html', **context)


class ImportQuestionsView(TemplatedView):
    def get(self):
        from app.migrations.question_migration import import_questions
        import_questions()
        self.response.out.write('Migration done. <button onclick="history.back()">Go back</button>')
