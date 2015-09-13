"""
Question model tests.
"""
from app.models.question import Question
from test.fixtures.appengine import GaeTestCase

class QuestionModelTests(GaeTestCase):
    def setUp(self):
        super(QuestionModelTests, self).setUp()

        self.question1 = Question()
        self.question1.text = 'Fake text'
        self.question1.category = 'adm'
        self.question1.question_number = 120
        self.question1.put()

    def test_pretty_category_returns_properly(self):
        self.assertEqual('Administration (Leadership)', self.question1.pretty_category)
