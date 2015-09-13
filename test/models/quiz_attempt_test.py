""" Tests for quiz attempts """
from random import randint

from app.models.question import Question
from app.models.quiz_attempt import QuizAttempt

from test.fixtures.appengine import GaeTestCase

class QuizAttemptTests(GaeTestCase):
    def setUp(self):
        super(QuizAttemptTests, self).setUp()

        self.categories = ["adm", "apo", "cou", "dis", "eva", "fai", "giv", "hea",
                      "int", "kno"]

        self.attempt = QuizAttempt(user_id=1)
        questions = []
        for i in range(0, 20):
            questions.append({
                'question_number': i + 1,
                'answer': randint(0, 2),
                'category': self.categories[i % 10]
            })
        self.attempt.questions = questions

    def test_top_categories_returns_aggregated_data_for_categories(self):
        top_cats = self.attempt.top_categories
        # Even though there are 20 questions from the different categories,
        # they should be combined into just 10 top category figures.
        self.assertEqual(len(self.categories), len(top_cats))

    def test_convert_points_converts_per_business_requirements(self):
        # 0 is 0, 1 is worth 2, and 2 is worth 5
        self.assertEqual(0, QuizAttempt.convert_points(0))
        self.assertEqual(2, QuizAttempt.convert_points(1))
        self.assertEqual(5, QuizAttempt.convert_points(2))
