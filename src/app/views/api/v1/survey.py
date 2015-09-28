"""
APIs for surveys
"""
from app.domain.questions import get_survey_page_for_user_id
from app.views.api import JsonApiHandler


class SurveyPageApiHandler(JsonApiHandler):
    """
    API for getting pages of surveys
    """

    def get(self, user_id, page_num):
        questions = get_survey_page_for_user_id(int(page_num), int(user_id))
        self.return_json_response(questions)
