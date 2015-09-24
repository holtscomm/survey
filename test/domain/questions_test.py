"""
Tests for domain methods in questions.py
"""
from app.domain.questions import get_survey_page
from app.migrations.question_migration import import_questions
from test.fixtures.appengine import GaeTestCase


class GetSurveyPageTests(GaeTestCase):

    def setUp(self):
        super(GetSurveyPageTests, self).setUp()
        # import_questions()

    def test_page_num_is_required(self):
        with self.assertRaises(ValueError):
            get_survey_page(None)

    def test_page_num_must_be_positive_integer(self):
        with self.assertRaises(ValueError):
            get_survey_page(-1)

    # @mock.patch('app.models.question.Question.get_questions_by_number_range')
    def test_page_num_1_returns_questions_1_to_20(self, questions_mock):
        get_survey_page(1)
        # self.assertEqual(1, questions[0].question_number)
        # self.assertEqual(20, questions[-1].question_number)
        questions_mock.assert_called_with(from_number=1, to_number=20)

    def test_page_num_2_returns_questions_21_to_40(self):
        questions = get_survey_page(2)
        self.assertEqual(21, questions[0].question_number)
        self.assertEqual(40, questions[-1].question_number)

    def test_page_num_4_returns_questions_61_to_80(self):
        questions = get_survey_page(4)
        self.assertEqual(61, questions[0].question_number)
        self.assertEqual(80, questions[-1].question_number)
