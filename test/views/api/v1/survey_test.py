"""
Tests for v1 of Survey API
"""
import mock
from app.views.api.v1.survey import SurveyPageApiHandler
from test.fixtures.appengine import GaeTestCase


class SurveyPageApiHandlerTests(GaeTestCase):

    def setUp(self):
        super(SurveyPageApiHandlerTests, self).setUp()

        self.handler = SurveyPageApiHandler()

    @mock.patch('app.views.api.v1.survey.get_survey_page_for_user_id')
    @mock.patch('app.views.api.v1.survey.SurveyPageApiHandler.return_json_response')
    def test_prevPage_and_nextPage_set_appropriately(self, json_mock, survey_mock):
        survey_mock.return_value = {}
        self.handler.get(1, 1)
        json_mock.assert_called_once_with(mock.ANY, additional_info={'prevPage': 1, 'nextPage': 2})

    @mock.patch('app.views.api.v1.survey.get_survey_page_for_user_id')
    @mock.patch('app.views.api.v1.survey.SurveyPageApiHandler.return_json_response')
    def test_prevPage_and_nextPage_set_appropriately_when_page_greater_than_one(self, json_mock, survey_mock):
        survey_mock.return_value = {}
        self.handler.get(1, 5)
        json_mock.assert_called_once_with(mock.ANY, additional_info={'prevPage': 4, 'nextPage': 6})

    @mock.patch('app.views.api.v1.survey.get_survey_page_for_user_id')
    @mock.patch('app.views.api.v1.survey.SurveyPageApiHandler.return_json_response')
    def test_nextPage_is_false_when_no_more_pages_to_return(self, json_mock, survey_mock):
        survey_mock.return_value = {}
        self.handler.get(1, 9)  # Max page for now, pretty bad way to do it.
        json_mock.assert_called_once_with(mock.ANY, additional_info={'prevPage': 8, 'nextPage': False})
