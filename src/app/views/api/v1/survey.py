"""
APIs for surveys
"""
import json

from app.domain.questions import get_survey_page_for_user_id, save_user_submitted_answers
from app.views.api import JsonApiHandler


class SurveyPageApiHandler(JsonApiHandler):
    """
    API for getting pages of surveys
    """

    def get(self, user_id, page_num):
        questions, prev_page, next_page = get_survey_page_for_user_id(int(page_num), int(user_id))
        response_data = {
            'prevPage': prev_page,
            'nextPage': next_page,
        }
        self.return_json_response(questions, additional_info=response_data)

    def post(self, user_id):
        submitted = json.loads(self.request.POST.get('questions'))
        save_user_submitted_answers(int(user_id), submitted)
        self.return_json_response(True)
