"""
APIs for surveys
"""
import json
import logging
import urlparse

from google.appengine.ext import deferred

from app.domain.survey import survey_for_type, survey_for_type_and_user
from app.models.quiz_attempt import QuizAttemptAnswer
from app.views.api import JsonApiHandler
from app.domain.purchase import Purchase, create_new_premium_user, send_email_with_survey_link


class SurveyGetFirstPageApiHandler(JsonApiHandler):
    """
    API that gets the first page for a user, somewhat implicitly for now.
    """
    def get(self):
        user_id = self.request.GET.get('userId', 1)
        quiz_type = self.request.GET.get('quizType', 'fullform')

        survey = survey_for_type_and_user(user_id, quiz_type)

        questions, prev_page, next_page = survey.get_survey_page(survey.first_page)
        response_data = {
            'userId': user_id,
            'prevPage': prev_page,
            'nextPage': next_page,
        }
        self.return_json_response(questions, additional_info=response_data)


class SurveyPageApiHandler(JsonApiHandler):
    """
    API for getting pages of surveys
    """
    def get(self, user_id, page_num):
        quiz_type = self.request.GET.get('quizType', 'fullform')
        questions, prev_page, next_page = survey_for_type_and_user(user_id, quiz_type).get_survey_page(int(page_num))
        response_data = {
            'prevPage': prev_page,
            'nextPage': next_page,
        }
        self.return_json_response(questions, additional_info=response_data)

    def post(self, user_id=None):
        quiz_type = self.request.GET.get('quizType', 'fullform')
        submitted = json.loads(self.request.body)
        survey_for_type(quiz_type)(user_id).save_user_submitted_answers(_normalize_data(submitted))
        self.return_json_response(True)


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


class SurveyPurchaseApiHandler(JsonApiHandler):
    """
    API for purchasing surveys
    """
    def post(self):
        new_purchase = Purchase(urlparse.parse_qs(self.request.body))
        logging.info('Someone bought the survey! %s %s %s %s %s', new_purchase.email, new_purchase.first_name,
                     new_purchase.last_name, new_purchase.product, new_purchase.purchase_date)
        logging.info('Deferring task to create new purchase and send email')
        user = create_new_premium_user(new_purchase)
        deferred.defer(send_email_with_survey_link, user.email, new_purchase.full_name, new_purchase.product,
                       user.user_id)

        self.return_json_response({'user_id': user.user_id})

