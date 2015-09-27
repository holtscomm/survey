"""
Tests for domain methods in questions.py
"""
import mock

from app.domain.questions import get_survey_page, get_survey_page_for_user_id
from app.models.question import Question
from test.fixtures.appengine import GaeTestCase


class GetSurveyPageTests(GaeTestCase):

    def test_page_num_is_required(self):
        with self.assertRaises(ValueError):
            get_survey_page(None)

    def test_page_num_must_be_positive_integer(self):
        with self.assertRaises(ValueError):
            get_survey_page(-1)

    @mock.patch('app.domain.questions.Question.get_questions_by_number_range')
    def test_page_num_1_returns_questions_1_to_20(self, questions_mock):
        get_survey_page(1)
        questions_mock.assert_called_once_with(1, 20)

    @mock.patch('app.domain.questions.Question.get_questions_by_number_range')
    def test_page_num_2_returns_questions_21_to_40(self, questions_mock):
        get_survey_page(2)
        questions_mock.assert_called_once_with(21, 40)

    @mock.patch('app.domain.questions.Question.get_questions_by_number_range')
    def test_page_num_4_returns_questions_61_to_80(self, questions_mock):
        get_survey_page(4)
        questions_mock.assert_called_once_with(61, 80)


class GetSurveyPageForUserIdTests(GaeTestCase):

    def setUp(self):
        super(GetSurveyPageForUserIdTests, self).setUp()

        self.question1 = Question()
        self.question1.text = 'Fake text'
        self.question1.category = 'adm'
        self.question1.question_number = 1
        self.question2 = Question()
        self.question2.text = 'Fake text'
        self.question2.category = 'fai'
        self.question2.question_number = 2

    @mock.patch('app.domain.questions.get_survey_page')
    def test_get_survey_page_gets_called(self, survey_mock):
        get_survey_page_for_user_id(1, 1)
        survey_mock.assert_called_once_with(1)

    @mock.patch('app.domain.questions.QuizAttempt.get_by_user_id')
    def test_gets_the_quiz_attempt_for_the_user_id_param(self, attempt_mock):
        get_survey_page_for_user_id(1, 1)
        attempt_mock.assert_called_once_with(1)

    @mock.patch('app.domain.questions.QuizAttempt.get_by_user_id')
    @mock.patch('app.domain.questions.Question.get_questions_by_number_range')
    def test_fills_in_answers_and_returns_list_of_dictionaries(self, questions_mock, attempt_mock):

        questions_mock.return_value = [
            self.question1,
            self.question2
        ]
        attempt_mock.return_value.questions = [
            {
                "question_number": 1,
                "text": "Fake text",
                "answer": 0,
                "category": "adm",
            },
            {
                "question_number": 2,
                "text": "Fake text",
                "answer": 5,
                "category": "fai",
            }
        ]
        actual = get_survey_page_for_user_id(1, 1)
        expected = [
            {
                "question_number": 1,
                "text": "Fake text",
                "answer": 0,
                "category": "adm"
            },
            {
                "question_number": 2,
                "text": "Fake text",
                "answer": 5,
                "category": "fai",
            }
        ]
        self.assertEqual(expected, actual)

    @mock.patch('app.domain.questions.Question.get_questions_by_number_range')
    def test_answers_are_zero_if_user_attempt_is_none(self, questions_mock):
        questions_mock.return_value = [
            self.question1,
            self.question2
        ]

        actual = get_survey_page_for_user_id(1, 1)
        expected = [
            {
                "question_number": 1,
                "text": "Fake text",
                "answer": 0,
                "category": "adm"
            },
            {
                "question_number": 2,
                "text": "Fake text",
                "answer": 0,
                "category": "fai",
            }
        ]
        self.assertEqual(expected, actual)
