"""
APIs for surveys
"""
from flask import Flask, Blueprint, request
import json
import logging
from urllib import parse

from google.cloud import ndb

from app.domain.survey import survey_for_type, survey_for_type_and_user
from app.models.quiz_attempt import QuizAttemptAnswer
from app.views.api import return_json_response
from app.domain.purchase import Purchase, create_new_premium_user, send_email_with_survey_link

client = ndb.Client()

bp = Blueprint('api', __name__, url_prefix='/api/v1/survey')

@bp.route('/getFirstPage/', methods=['GET'])
def first_page_handler():
    """
    API that gets the first page for a user, somewhat implicitly for now.
    """
    with client.context():
        user_id = request.args.get('userId', 1)
        quiz_type = request.args.get('quizType', 'fullform')

        survey = survey_for_type_and_user(user_id, quiz_type)

        questions, prev_page, next_page = survey.get_survey_page(survey.first_page)
        response_data = {
            'userId': user_id,
            'prevPage': prev_page,
            'nextPage': next_page,
        }
        return return_json_response(questions, additional_info=response_data)

@bp.route('/<user_id>/<page_num>/', methods=['GET'])
def get_survey_page(user_id, page_num):
    """
    API for getting pages of surveys
    """
    with client.context():
        quiz_type = request.args.get('quizType', 'fullform')
        questions, prev_page, next_page = survey_for_type_and_user(user_id, quiz_type).get_survey_page(int(page_num))
        response_data = {
            'prevPage': prev_page,
            'nextPage': next_page,
        }
        return return_json_response(questions, additional_info=response_data)


@bp.route('/post/<user_id>/', methods=['POST'])
def handle_survey_page(user_id=None):
    with client.context():
        quiz_type = request.args.get('quizType', 'fullform')
        submitted = json.loads(request.data)
        survey_for_type(quiz_type)(user_id).save_user_submitted_answers(_normalize_data(submitted))
        return return_json_response(True)


def _normalize_data(json_answers):
    """
    Takes the json loads'd data from Javascript and converts it to what save_user_submitted_answers will expect.
    :return: list of dictionaries
    :rtype: list
    """
    answers = []
    for question_number in json_answers.keys():
        category_answer = json_answers[question_number].split(':')
        answers.append(QuizAttemptAnswer(
            question_number=int(question_number),
            category=category_answer[0],
            answer=int(category_answer[1])
        ))

    return sorted(answers, cmp=lambda x, y: cmp(x.question_number, y.question_number))

@bp.route('/purchase/', methods=['POST'])
def handle_survey_purchase():
    """
    API for purchasing surveys
    """
    new_purchase = Purchase(parse.parse_qs(request.get_data()))
    logging.info('Someone bought the survey! %s %s %s %s %s', new_purchase.email, new_purchase.first_name,
                    new_purchase.last_name, new_purchase.product, new_purchase.purchase_date)
    logging.info('Deferring task to create new purchase and send email')
    with client.context():
        user = create_new_premium_user(new_purchase)
        try:
            send_email_with_survey_link(user.email, new_purchase.full_name, new_purchase.product, user.user_id)
        except Exception as e:
            print(e)
            # let things keep rolling though

        return return_json_response({'user_id': user.user_id})

