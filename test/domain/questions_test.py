"""
Tests for domain methods in questions.py
"""
import mock

from app.domain.questions import get_survey_page
from test.fixtures.appengine import GaeTestCase


class GetSurveyPageTests(GaeTestCase):

    def test_page_num_is_required(self):
        with self.assertRaises(ValueError):
            get_survey_page(None)

    def test_page_num_must_be_positive_integer(self):
        with self.assertRaises(ValueError):
            get_survey_page(-1)

    @mock.patch('app.models.question.Question.get_questions_by_number_range')
    def test_page_num_1_returns_questions_1_to_20(self, questions_mock):
        get_survey_page(1)
        questions_mock.assert_called_once_with(1, 20)

    @mock.patch('app.models.question.Question.get_questions_by_number_range')
    def test_page_num_2_returns_questions_21_to_40(self, questions_mock):
        get_survey_page(2)
        questions_mock.assert_called_once_with(21, 40)

    @mock.patch('app.models.question.Question.get_questions_by_number_range')
    def test_page_num_4_returns_questions_61_to_80(self, questions_mock):
        get_survey_page(4)
        questions_mock.assert_called_once_with(61, 80)
