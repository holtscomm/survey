"""
Tests for domain methods in questions.py
"""
from app.domain.questions import get_survey_page
from app.migrations.question_migration import import_questions
from test.fixtures.appengine import GaeTestCase


class GetSurveyPageTests(GaeTestCase):

    def setUp(self):
        super(GetSurveyPageTests, self).setUp()
        import_questions()

    def test_page_num_is_required(self):
        with self.assertRaises(ValueError):
            get_survey_page(None)

    def test_page_num_must_be_positive_integer(self):
        with self.assertRaises(ValueError):
            get_survey_page(-1)

    def test_page_num_1_returns_questions_1_to_20(self):
        questions = get_survey_page(1)
        self.assertEqual(1, questions[0].question_number)
        self.assertEqual(20, questions[-1].question_number)
