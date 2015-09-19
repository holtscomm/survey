""" Tests for quiz attempts """
from random import randint
from app.models.question import Question

from app.models.quiz_attempt import QuizAttempt

from test.fixtures.appengine import GaeTestCase


class QuizAttemptTests(GaeTestCase):
    def setUp(self):
        super(QuizAttemptTests, self).setUp()

        self.categories = ["adm", "apo", "cou", "dis", "eva", "fai", "giv", "hea", "int", "kno"]

        self.attempt = QuizAttempt(user_id=1)
        questions = []
        for i in range(0, 20):
            questions.append({
                'question_number': i + 1,
                'answer': randint(0, 2),
                'category': self.categories[i % 10]
            })
        self.attempt.questions = questions
        self.attempt.put()

    def test_graded_categories_returns_aggregated_data_for_categories(self):
        self.assertEqual(len(Question.CATEGORY_MAPPINGS), len(self.attempt.graded_categories))

    def test_graded_categories_come_in_sorted_order(self):
        graded_cats = self.attempt.graded_categories
        self.assertLessEqual(graded_cats[1][1], graded_cats[0][1])
        self.assertLessEqual(graded_cats[2][1], graded_cats[1][1])

    def test_convert_points_converts_per_business_requirements(self):
        # 0 is 0, 1 is worth 2, and 2 is worth 5
        self.assertEqual(0, QuizAttempt.convert_points(0))
        self.assertEqual(2, QuizAttempt.convert_points(1))
        self.assertEqual(5, QuizAttempt.convert_points(2))

    def test_get_by_user_id_returns_right_number_of_results(self):
        self.assertEqual(1, len(QuizAttempt.get_by_user_id(1)))
