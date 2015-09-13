""" Tests for questions domain logic """
from google.appengine.ext import ndb

from app.models.question import Question
from test.fixtures.appengine import GaeTestCase

class CalculateScoresTests(GaeTestCase):
    def setUp(self):
        super(CalculateScoresTests, self).setUp()

        self.question_list = []

        num = 1
        for question_category in Question.CATEGORY_MAPPINGS.keys():
            question1 = Question()
            question1.text = 'Fake text'
            question1.category = question_category
            question1.question_number = num
            self.question_list.append(question1)
            num += 1
            question2 = Question()
            question2.text = 'Fake text'
            question2.category = question_category
            question2.question_number = num
            num += 1
            self.question_list.append(question2)
