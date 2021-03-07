""" superadmin.py """
from flask import Blueprint, render_template_string, session, redirect

from google.cloud import ndb

client = ndb.Client()

import settings
from app.models.question import Question
from app.models.quiz_attempt import QuizAttempt
from app.models.user import User
from app.views import render_survey_template


bp = Blueprint('superadmin', __name__, url_prefix='/superadmin')


@ndb.synctasklet
def get_superadmin_index_data():
    paid_survey_users, all_quiz_attempts, paid_quiz_attempts = yield (
        User.get_paid_survey_users().fetch_async(),
        QuizAttempt.get_all_attempts().fetch_async(),
        QuizAttempt.get_non_trial_attempts().fetch_async()
    )
    all_users = []
    quiz_attempt_dicts = []
    for attempt in all_quiz_attempts:
        user = User.build_key(attempt.user_id).get()
        quiz_attempt_dicts.append({
            'attempt': attempt,
            'user': user
        })
        all_users.append(user)
    raise ndb.Return((paid_survey_users, quiz_attempt_dicts, all_users, paid_quiz_attempts))


@bp.route('/')
def superadmin_index():
    if 'credentials' not in session:
        return redirect('/auth/login')
    with client.context():
        paid_survey_users, all_quiz_attempts, all_users, paid_quiz_attempts = get_superadmin_index_data()

        context = {
            'paid_survey_users': len(paid_survey_users),
            # 'paid_survey_users_last_30_days': len(User.get_paid_survey_users_last_30_days().fetch())
            'quiz_attempt_data': all_quiz_attempts,
            'all_users': all_users,
            'paid_quiz_attempts': paid_quiz_attempts,
            'env': 'local' if settings.is_devappserver() else 'not-local'
        }

        return render_survey_template('superadmin/index.html', **context)


@bp.route('/generate/')
def generate_survey():
    if 'credentials' not in session:
        return redirect('/auth/login')
    print(session)
    return render_survey_template('superadmin/generate.html')


@bp.route('/questions/')
def print_questions():
    if 'credentials' not in session:
        return redirect('/auth/login')
    with client.context():
        context = {
            'questions': Question.get_all_questions(ordered=True)
        }

        return render_survey_template('superadmin/print_questions.html', **context)


@bp.route('/import/')
def import_questions():
    if 'credentials' not in session:
        return redirect('/auth/login')
    from app.migrations.question_migration import import_questions
    with client.context():
        import_questions()
        return render_template_string('Migration done. <button onclick="history.back()">Go back</button>')
