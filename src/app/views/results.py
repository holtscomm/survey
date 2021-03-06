""" Results views """
from flask import Blueprint, request
from google.cloud import ndb

client = ndb.Client()

from app.models.user import User
from app.models.quiz_attempt import QuizAttempt
from app.views import render_survey_template

bp = Blueprint('results', __name__, url_prefix='/results')

@ndb.synctasklet
def get_results_data(user_id):
    """ Get the results needed for the survey page """
    users, quiz_attempts = yield(
        User.get_by_user_id_async(user_id),
        QuizAttempt.get_all_attempts_for_user_id_async(user_id)
    )
    raise ndb.Return((users, quiz_attempts))

@bp.route('/', methods=['GET'])
def get_results():
    """ GET """
    user_id = request.args.get('userId', 1)
    with client.context():
        user, quiz_attempts = get_results_data(user_id)

        context = {
            'user': user,
            'quiz_attempts': quiz_attempts
        }

        return render_survey_template("results.html", **context)
