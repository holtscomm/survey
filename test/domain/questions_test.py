"""
Tests for domain methods in questions.py
"""
import mock

from app.domain.questions import get_survey_page, get_survey_page_for_user_id, save_user_submitted_answers
from app.models.question import Question
from app.models.quiz_attempt import QuizAttempt, QuizAttemptAnswer
from test.fixtures.appengine import GaeTestCase


class GetSurveyPageTests(GaeTestCase):

    def test_page_num_is_required(self):
        with self.assertRaises(ValueError):
            get_survey_page(None)

    def test_page_num_must_be_positive_integer(self):
        with self.assertRaises(ValueError):
            get_survey_page(-1)

    def test_page_num_can_not_be_string_one(self):
        with self.assertRaises(ValueError):
            get_survey_page("one")

    @mock.patch('app.domain.questions._calculate_from_and_to_for_page_number')
    def test_page_num_is_converted_to_integer(self, number_mock):
        number_mock.return_value = (1, 20)
        get_survey_page("1")
        number_mock.assert_called_once_with(1)

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
            QuizAttemptAnswer(question_number=1, answer=0),
            QuizAttemptAnswer(question_number=2, answer=5)
        ]
        actual, _, _ = get_survey_page_for_user_id(1, 1)
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
    def test_answers_are_None_if_user_attempt_is_none(self, questions_mock):
        questions_mock.return_value = [
            self.question1,
            self.question2
        ]

        actual, _, _ = get_survey_page_for_user_id(1, 1)
        expected = [
            {
                "question_number": 1,
                "text": "Fake text",
                "answer": None,
                "category": "adm"
            },
            {
                "question_number": 2,
                "text": "Fake text",
                "answer": None,
                "category": "fai",
            }
        ]
        self.assertEqual(expected, actual)

    @mock.patch('app.domain.questions.QuizAttempt.get_by_user_id')
    @mock.patch('app.domain.questions.Question.get_questions_by_number_range')
    def test_None_returned_after_end_of_questions_user_has_already_answered(self, questions_mock, attempt_mock):
        question3 = Question(text="Something", question_number=3, category="adm")
        questions_mock.return_value = [
            self.question1,
            self.question2,
            question3
        ]

        attempt_mock.return_value.questions = [
            QuizAttemptAnswer(question_number=1, answer=0),
            QuizAttemptAnswer(question_number=2, answer=5)
        ]

        actual, _, _ = get_survey_page_for_user_id(1, 1)
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
            },
            {
                "question_number": 3,
                "text": "Something",
                "answer": None,
                "category": "adm",
            }
        ]
        self.assertEqual(expected, actual)

    @mock.patch('app.domain.questions.Question.get_questions_by_number_range')
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

        actual, _, _ = get_survey_page_for_user_id(2, 1)
        expected = [
            {
                "question_number": 21,
                "text": "Fake text",
                "answer": None,
                "category": "adm"
            },
            {
                "question_number": 22,
                "text": "Fake text",
                "answer": None,
                "category": "fai",
            }
        ]
        self.assertEqual(expected, actual)

    @mock.patch('app.domain.questions.QuizAttempt.get_by_user_id')
    @mock.patch('app.domain.questions.Question.get_questions_by_number_range')
    def test_correct_answers_returned_with_page_greater_than_one(self, questions_mock, attempt_mock):
        question21 = Question()
        question21.text = "Fake text"
        question21.category = "adm"
        question21.question_number = 41
        question22 = Question()
        question22.text = "Fake text"
        question22.category = "fai"
        question22.question_number = 42

        questions_mock.return_value = [
            question21,
            question22
        ]

        attempt_mock.return_value.questions = [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10,  # Need to add all of these because in theory they would be here.
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            QuizAttemptAnswer(question_number=41, answer=0),
            QuizAttemptAnswer(question_number=42, answer=5)
        ]

        actual, _, _ = get_survey_page_for_user_id(3, 1)
        expected = [
            {
                "question_number": 41,
                "text": "Fake text",
                "answer": 0,
                "category": "adm"
            },
            {
                "question_number": 42,
                "text": "Fake text",
                "answer": 5,
                "category": "fai",
            }
        ]
        self.assertEqual(expected, actual)

    @mock.patch('app.domain.questions.get_survey_page')
    def test_prevPage_and_nextPage_set_appropriately(self, survey_mock):
        survey_mock.return_value = []
        _, prev_p, next_p = get_survey_page_for_user_id(1, 1)
        self.assertEqual(1, prev_p)
        self.assertEqual(2, next_p)

    @mock.patch('app.domain.questions.get_survey_page')
    def test_prevPage_and_nextPage_set_appropriately_when_page_greater_than_one(self, survey_mock):
        survey_mock.return_value = []
        _, prev_p, next_p = get_survey_page_for_user_id(5, 1)
        self.assertEqual(4, prev_p)
        self.assertEqual(6, next_p)

    @mock.patch('app.domain.questions.get_survey_page')
    def test_nextPage_is_false_when_no_more_pages_to_return(self, survey_mock):
        survey_mock.return_value = []
        _, prev_p, next_p = get_survey_page_for_user_id(9, 1)
        self.assertEqual(8, prev_p)
        self.assertEqual(False, next_p)


class SaveUserSubmittedAnswersTests(GaeTestCase):
    @mock.patch('app.domain.questions.QuizAttempt.get_by_user_id')
    def test_previous_quiz_attempt_by_user_passed_in_is_retrieved(self, attempt_mock):
        save_user_submitted_answers(1, [])
        attempt_mock.assert_called_once_with(1)

    @mock.patch('app.domain.questions.QuizAttempt.get_by_user_id')
    def test_saves_all_answers_to_attempt_if_user_attempt_is_empty_for_those_questions(self, attempt_mock):
        attempt = QuizAttempt(user_id=1, questions=[])
        attempt_mock.return_value = attempt
        save_user_submitted_answers(1, [QuizAttemptAnswer(question_number=1, answer=5)])
        self.assertEqual(1, len(attempt.questions))

    @mock.patch('app.domain.questions.QuizAttempt.get_by_user_id')
    def test_saves_answers_over_any_attempt_answers_that_already_exist(self, attempt_mock):
        attempt = QuizAttempt(user_id=1, questions=[
            QuizAttemptAnswer(question_number=1, answer=0, category='adm'),
            QuizAttemptAnswer(question_number=2, answer=5, category='adm'),
        ])
        attempt_mock.return_value = attempt
        save_user_submitted_answers(1, [
            QuizAttemptAnswer(question_number=1, answer=5),
            QuizAttemptAnswer(question_number=2, answer=2),
        ])
        self.assertEqual(5, attempt.questions[0].answer)
        self.assertEqual(2, attempt.questions[1].answer)

    @mock.patch('app.domain.questions.QuizAttempt.get_by_user_id')
    def test_extends_quiz_attempt_with_any_new_answers(self, attempt_mock):
        attempt = QuizAttempt(user_id=1, questions=[
            QuizAttemptAnswer(question_number=1, answer=0),
            QuizAttemptAnswer(question_number=2, answer=0),
            QuizAttemptAnswer(question_number=3, answer=0),
            QuizAttemptAnswer(question_number=4, answer=0),
            QuizAttemptAnswer(question_number=5, answer=0),
        ])
        attempt_mock.return_value = attempt
        save_user_submitted_answers(1, [
            QuizAttemptAnswer(question_number=5, answer=5),
            QuizAttemptAnswer(question_number=6, answer=0),
            QuizAttemptAnswer(question_number=7, answer=5),
            QuizAttemptAnswer(question_number=8, answer=2),
            QuizAttemptAnswer(question_number=9, answer=2),
            QuizAttemptAnswer(question_number=10, answer=5),
        ])
        self.assertEqual(5, attempt.questions[4].answer)
        self.assertEqual(10, len(attempt.questions))
