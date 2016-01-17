""" Tests for Question domain object """
import unittest

import mock

from app.domain.survey import Survey, ShortASurvey, survey_for_type, ShortBSurvey
from app.models.question import Question
from app.models.quiz_attempt import QuizAttempt, QuizAttemptAnswer
from test.fixtures.appengine import GaeTestCase


class SurveyTests(GaeTestCase):
    def setUp(self, consistent=True, urlfetch=False):
        super(SurveyTests, self).setUp(consistent, urlfetch)
        self.survey = Survey(1)

        self.question1 = Question()
        self.question1.text = 'Fake text'
        self.question1.category = 'adm'
        self.question1.question_number = 1
        self.question2 = Question()
        self.question2.text = 'Fake text'
        self.question2.category = 'fai'
        self.question2.question_number = 2

    def test_survey_requires_user_id(self):
        with self.assertRaises(ValueError):
            Survey(None)

    def test_first_page_property_returns_first_20_questions_for_new_user_id(self):
        QuizAttempt.create(1)
        self.assertEqual(1, self.survey.first_page)

    @mock.patch('app.domain.survey.QuizAttempt.get_by_user_id')
    def test_previous_quiz_attempt_by_user_passed_in_is_retrieved(self, quiz_attempt_get_by_user_id_mock):
        self.survey.save_user_submitted_answers([])
        quiz_attempt_get_by_user_id_mock.assert_called_once_with(1, 'fullform')

    @mock.patch('app.domain.survey.QuizAttempt.get_by_user_id')
    def test_saves_all_answers_to_attempt_if_user_attempt_is_empty_for_those_questions(self,
                                                                                       quiz_attempt_get_by_user_id_mock
                                                                                       ):
        attempt = QuizAttempt(user_id=1, questions=[])
        quiz_attempt_get_by_user_id_mock.return_value = attempt
        self.survey.save_user_submitted_answers([QuizAttemptAnswer(question_number=1, answer=5)])
        self.assertEqual(1, len(attempt.questions))

    @mock.patch('app.domain.survey.QuizAttempt.get_by_user_id')
    def test_saves_answers_over_any_attempt_answers_that_already_exist(self, quiz_attempt_get_by_user_id_mock):
        attempt = QuizAttempt(user_id=1, questions=[
            QuizAttemptAnswer(question_number=1, answer=0, category='adm'),
            QuizAttemptAnswer(question_number=2, answer=5, category='adm'),
        ])
        quiz_attempt_get_by_user_id_mock.return_value = attempt
        self.survey.save_user_submitted_answers([
            QuizAttemptAnswer(question_number=1, answer=5),
            QuizAttemptAnswer(question_number=2, answer=2),
        ])
        self.assertEqual(5, attempt.questions[0].answer)
        self.assertEqual(2, attempt.questions[1].answer)

    @mock.patch('app.domain.survey.QuizAttempt.get_by_user_id')
    def test_extends_quiz_attempt_with_any_new_answers(self, quiz_attempt_get_by_user_id_mock):
        attempt = QuizAttempt(user_id=1, questions=[
            QuizAttemptAnswer(question_number=1, answer=0),
            QuizAttemptAnswer(question_number=2, answer=0),
            QuizAttemptAnswer(question_number=3, answer=0),
            QuizAttemptAnswer(question_number=4, answer=0),
            QuizAttemptAnswer(question_number=5, answer=0),
        ])
        quiz_attempt_get_by_user_id_mock.return_value = attempt
        self.survey.save_user_submitted_answers([
            QuizAttemptAnswer(question_number=5, answer=5),
            QuizAttemptAnswer(question_number=6, answer=0),
            QuizAttemptAnswer(question_number=7, answer=5),
            QuizAttemptAnswer(question_number=8, answer=2),
            QuizAttemptAnswer(question_number=9, answer=2),
            QuizAttemptAnswer(question_number=10, answer=5),
        ])
        self.assertEqual(5, attempt.questions[4].answer)
        self.assertEqual(10, len(attempt.questions))

    @mock.patch('app.domain.survey.QuizAttempt.get_by_user_id')
    def test_answer_not_written_if_question_numbers_dont_match(self, quiz_attempt_get_by_user_id_mock):
        attempt = QuizAttempt(user_id=1, questions=[
            QuizAttemptAnswer(question_number=1, answer=0),
            QuizAttemptAnswer(question_number=2, answer=0),
            QuizAttemptAnswer(question_number=3, answer=0),
        ])
        quiz_attempt_get_by_user_id_mock.return_value = attempt
        self.survey.save_user_submitted_answers([
            QuizAttemptAnswer(question_number=1, answer=2),
            QuizAttemptAnswer(question_number=3, answer=5),
            QuizAttemptAnswer(question_number=4, answer=5),
        ])
        self.assertEqual(0, attempt.questions[1].answer)
        self.assertEqual(5, attempt.questions[2].answer)
        self.assertEqual(5, attempt.questions[3].answer)

    def test_page_num_is_required(self):
        with self.assertRaises(ValueError):
            self.survey._get_questions_for_survey_page(None)

    def test_page_num_must_be_positive_integer(self):
        with self.assertRaises(ValueError):
            self.survey._get_questions_for_survey_page(-1)

    def test_page_num_can_not_be_string_one(self):
        with self.assertRaises(ValueError):
            self.survey._get_questions_for_survey_page("one")

    @mock.patch('app.domain.survey.Survey._calculate_from_and_to_for_page_number')
    def test_page_num_is_converted_to_integer(self, calculate_page_number_mock):
        calculate_page_number_mock.return_value = (1, 15)
        self.survey._get_questions_for_survey_page("1")
        calculate_page_number_mock.assert_called_once_with(1)

    @mock.patch('app.domain.survey.Question.get_questions_by_number_range')
    def test_page_num_1_returns_questions_1_to_20(self, get_questions_by_number_range_mock):
        self.survey._get_questions_for_survey_page(1)
        get_questions_by_number_range_mock.assert_called_once_with(1, 15)

    @mock.patch('app.domain.survey.Question.get_questions_by_number_range')
    def test_page_num_2_returns_questions_21_to_40(self, get_questions_by_number_range_mock):
        self.survey._get_questions_for_survey_page(2)
        get_questions_by_number_range_mock.assert_called_once_with(16, 30)

    @mock.patch('app.domain.survey.Question.get_questions_by_number_range')
    def test_page_num_4_returns_questions_61_to_80(self, get_questions_by_number_range_mock):
        self.survey._get_questions_for_survey_page(4)
        get_questions_by_number_range_mock.assert_called_once_with(46, 60)

    @mock.patch('app.domain.survey.Survey._get_questions_for_survey_page')
    def test_get_survey_page_gets_called(self, get_survey_page_mock):
        self.survey.get_survey_page(1)
        get_survey_page_mock.assert_called_once_with(1)

    @mock.patch('app.domain.survey.Survey._get_questions_for_survey_page')
    def test_answers_are_None_if_user_attempt_is_none(self, questions_mock):
        questions_mock.return_value = [
            self.question1,
            self.question2
        ]

        actual, _, _ = self.survey.get_survey_page(1)
        expected = [
            {"question_number": 1, "text": "Fake text", "answer": None, "category": "adm"},
            {"question_number": 2, "text": "Fake text", "answer": None, "category": "fai"}
        ]
        self.assertEqual(expected, actual)

    @mock.patch('app.domain.survey.Question.get_questions_by_number_range')
    def test_correct_questions_returned_for_page_higher_than_one(self, questions_mock):
        question21 = Question()
        question21.text = "Fake text"
        question21.category = "adm"
        question21.question_number = 21
        question22 = Question()
        question22.text = "Fake text"
        question22.category = "fai"
        question22.question_number = 22

        questions_mock.return_value = [
            question21,
            question22
        ]

        actual, _, _ = self.survey.get_survey_page(2)
        expected = [
            {"question_number": 21, "text": "Fake text", "answer": None, "category": "adm"},
            {"question_number": 22, "text": "Fake text", "answer": None, "category": "fai"}
        ]
        self.assertEqual(expected, actual)

    @mock.patch('app.domain.survey.Survey._get_questions_for_survey_page')
    def test_prevPage_and_nextPage_set_appropriately(self, get_survey_page_mock):
        get_survey_page_mock.return_value = []
        _, prev_p, next_p = self.survey.get_survey_page(1)
        self.assertEqual(1, prev_p)
        self.assertEqual(2, next_p)

    @mock.patch('app.domain.survey.Survey._get_questions_for_survey_page')
    def test_prevPage_and_nextPage_set_appropriately_when_page_greater_than_one(self, get_survey_page_mock):
        get_survey_page_mock.return_value = []
        _, prev_p, next_p = self.survey.get_survey_page(5)
        self.assertEqual(4, prev_p)
        self.assertEqual(6, next_p)

    @mock.patch('app.domain.survey.Survey._get_questions_for_survey_page')
    def test_nextPage_is_false_when_no_more_pages_to_return(self, get_survey_page_mock):
        get_survey_page_mock.return_value = []
        _, prev_p, next_p = self.survey.get_survey_page(12)
        self.assertEqual(11, prev_p)
        self.assertEqual(False, next_p)

    @mock.patch('app.domain.survey.ShortASurvey._get_questions_for_survey_page')
    def test_nextPage_is_false_when_no_more_pages_to_return_on_short_quiz(self, get_survey_page_mock):
        get_survey_page_mock.return_value = []
        _, prev_p, next_p = ShortASurvey(1).get_survey_page(90 / 15)
        self.assertEqual(5, prev_p)
        self.assertEqual(False, next_p)

    def test_normalize_question_numbers_returns_question_list_unchanged(self):
        questions = [
            {'question_number': 1},
            {'question_number': 2},
            {'question_number': 3},
            {'question_number': 4},
            {'question_number': 5},
            {'question_number': 6},
            {'question_number': 7},
            {'question_number': 8},
            {'question_number': 9},
            {'question_number': 10},
            {'question_number': 11},
            {'question_number': 12},
            {'question_number': 13},
            {'question_number': 14},
            {'question_number': 15}
        ]
        normalized = self.survey._normalize_question_numbers(questions, 1)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                         [q['question_number'] for q in normalized])


class SurveyForTypeTests(unittest.TestCase):
    def test_ShortASurvey_returned_for_short_a_type(self):
        self.assertEqual(ShortASurvey, survey_for_type('short_a'))

    def test_ShortBSurvey_returned_for_short_b_type(self):
        self.assertEqual(ShortBSurvey, survey_for_type('short_b'))

    def test_Survey_returned_for_fullform_type(self):
        self.assertEqual(Survey, survey_for_type('fullform'))

    def test_Survey_returned_for_no_type(self):
        self.assertEqual(Survey, survey_for_type())


class ShortASurveyTests(unittest.TestCase):
    def setUp(self):
        super(ShortASurveyTests, self).setUp()
        self.questions = [
            {'question_number': 1},
            {'question_number': 3},
            {'question_number': 4},
            {'question_number': 6},
            {'question_number': 7},
            {'question_number': 9},
            {'question_number': 11},
            {'question_number': 12},
            {'question_number': 14},
            {'question_number': 15},
            {'question_number': 16},
            {'question_number': 17},
            {'question_number': 18},
            {'question_number': 19},
            {'question_number': 21}
        ]

        self.questions_in = [
            QuizAttemptAnswer(question_number=1),
            QuizAttemptAnswer(question_number=2),
            QuizAttemptAnswer(question_number=3),
            QuizAttemptAnswer(question_number=4),
            QuizAttemptAnswer(question_number=5),
            QuizAttemptAnswer(question_number=6),
            QuizAttemptAnswer(question_number=7),
            QuizAttemptAnswer(question_number=8),
            QuizAttemptAnswer(question_number=9),
            QuizAttemptAnswer(question_number=10),
            QuizAttemptAnswer(question_number=11),
            QuizAttemptAnswer(question_number=12),
            QuizAttemptAnswer(question_number=13),
            QuizAttemptAnswer(question_number=14),
            QuizAttemptAnswer(question_number=15),
        ]

    def test_normalize_question_numbers_out_returns_1_to_15_for_page_one(self):
        normalized = ShortASurvey(1)._normalize_question_numbers(self.questions, 1)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                         [q['question_number'] for q in normalized])

    def test_normalize_question_numbers_out_returns_16_to_30_for_page_two(self):
        normalized = ShortASurvey(1)._normalize_question_numbers(self.questions, 2)
        self.assertEqual([16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
                         [q['question_number'] for q in normalized])

    def test_normalize_question_numbers_in_returns_1_to_15_for_page_one(self):
        normalized = ShortASurvey(1)._normalize_question_numbers(self.questions_in, 1, False)
        self.assertEqual([2, 5, 8, 10, 13, 20, 22, 23, 25, 28, 30, 31, 32, 34, 35],
                         [q.question_number for q in normalized])

    def test_normalize_question_numbers_returns_questions_untouched_when_list_is_empty(self):
        self.assertEqual([], ShortASurvey(1)._normalize_question_numbers([], 1))
