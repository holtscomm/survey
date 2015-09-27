"""
APIs for surveys
"""
import webapp2
from app.domain.questions import get_survey_page_for_user_id


class SurveyPageApiHandler(webapp2.RequestHandler):
    """
    API for getting pages of surveys
    """

    def get(self, user_id, page_num):
        get_survey_page_for_user_id(page_num, user_id)
