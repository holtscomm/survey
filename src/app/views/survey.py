"""
Survey view
"""
from flask import Blueprint, request, render_template
import logging

from google.cloud import ndb

client = ndb.Client()

import settings
from app.models.user import User
from app.models.quiz_attempt import QuizAttempt
from app.views import render_survey_template

bp = Blueprint('gifts', __name__, url_prefix='/gifts')

def render_survey(**context):
    """ Survey base that other survey types inherit from """
    with client.context():
        user = User.get_or_create_by_user_id(request.args.get('userId'))
        attempt = QuizAttempt.get_by_user_id(user.user_id, context['quiz_type'])
        if not attempt:
            # Start up a new QuizAttempt!
            attempt = QuizAttempt.create(user_id=user.user_id, quiz_type=context['quiz_type'])
        if settings.is_devappserver():
            user.paid = True
        context.update({
            'user': user,
            'user_id': user.user_id,
            'quiz_attempt': attempt
        })

        logging.info(context)
        return render_survey_template('survey.html', **context)


@bp.route('/')
def full_survey():
    """ Full survey """
    context = {
        'request_path': '/gifts/',
        'quiz_type': 'fullform'
    }
    return render_survey(**context)


@bp.route('/a/')
def short_a():
    """ Short form A survey """
    context = {
        'request_path': '/gifts/a/',
        'quiz_type': 'short_a'
    }
    return render_survey(**context)


@bp.route('/b/')
def short_b():
    """ Short form B survey """
    context = {
        'quiz_type': 'short_b'
    }
    return render_survey(**context)


@bp.route('/trial/')
def trial():
    """ Trial survey """
    context = {
        'request_path': '/gifts/trial/',
        'quiz_type': 'trial'
    }
    return render_survey(**context)
