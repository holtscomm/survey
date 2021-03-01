"""
APIs for surveys
"""
from flask import Flask, Blueprint, request
import json
import logging
import urlparse

from google.cloud import ndb

from app.domain.survey import survey_for_type, survey_for_type_and_user
from app.models.quiz_attempt import QuizAttemptAnswer
from app.views.api import return_json_response
from app.domain.purchase import Purchase, create_new_premium_user, send_email_with_survey_link

client = ndb.Client()

bp = Blueprint('api', __name__, url_prefix='/api/v1/survey')

# Route('/api/v1/survey/<user_id:.+>/<page_num:\d+>/', handler='app.views.api.v1.survey.SurveyPageApiHandler'),
# Route('/api/v1/survey/getFirstPage/', handler='app.views.api.v1.survey.SurveyGetFirstPageApiHandler'),
# Route('/api/v1/survey/post/<user_id:.+>/', handler='app.views.api.v1.survey.SurveyPageApiHandler'),
# Route('/api/v1/survey/purchase/', handler='app.views.api.v1.survey.SurveyPurchaseApiHandler'),

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

# Route('/api/v1/survey/<user_id:.+>/<page_num:\d+>/', handler='app.views.api.v1.survey.SurveyPageApiHandler'),
@bp.route('/<user_id>/<page_num>', methods=['GET'])
def get_survey_page(self, user_id, page_num):
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


# Route('/api/v1/survey/post/<user_id:.+>/', handler='app.views.api.v1.survey.SurveyPageApiHandler'),
@bp.route('/post/<user_id>/', methods=['POST'])
def handle_survey_page(self, user_id=None):
    with client.context():
        quiz_type = request.args.get('quizType', 'fullform')
        # submitted = json.loads(self.request.body)
        # survey_for_type(quiz_type)(user_id).save_user_submitted_answers(_normalize_data(submitted))
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

# Route('/api/v1/survey/purchasee/', handler='app.views.api.v1.survey.SurveyPurchaseApiHandler'),
@bp.route('/purchase/', methods=['POST'])
def handle_survey_purchase(self):
    """
    API for purchasing surveys
    """
    new_purchase = Purchase(urlparse.parse_qs(self.request.body))
    logging.info('Someone bought the survey! %s %s %s %s %s', new_purchase.email, new_purchase.first_name,
                    new_purchase.last_name, new_purchase.product, new_purchase.purchase_date)
    logging.info('Deferring task to create new purchase and send email')
    with client.context():
        user = create_new_premium_user(new_purchase)
        send_email_with_survey_link(user.email, new_purchase.full_name, new_purchase.product, user.user_id)

        return return_json_respons({'user_id': user.user_id})

