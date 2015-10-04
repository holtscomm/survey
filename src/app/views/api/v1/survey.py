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
        int_page_num = int(page_num)
        questions = get_survey_page_for_user_id(int_page_num, int(user_id))
        response_data = {
            'prevPage': 1 if int_page_num == 1 else int_page_num - 1,
            'nextPage': False if int_page_num == 9 else int_page_num + 1,
        }
        self.return_json_response(questions, additional_info=response_data)
