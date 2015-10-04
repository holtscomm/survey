""" Quiz attempts model """
from google.appengine.ext import ndb

from .question import Question


class QuizAttempt(ndb.Model):
    """
    Stores information about a quiz attempt for a user. questions is a
    JsonProperty that looks something like this:

    questions = [
        {
            "question_number": 1,
            "answer": 0,
            "category": "adm"
        },
        ...
    ]
    """
    user_id = ndb.IntegerProperty()
    questions = ndb.JsonProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)

    @property
    def graded_categories(self):
        """
        These are the final categories that someone is in. In descending order.

        Returns a list of tuples like:
        [
            ("adm", 10),
            ("tea", 5),
            ...etc...
        ]
        :rtype: List
        """
        categories = []
        for category in Question.CATEGORY_MAPPINGS.keys():
            sum_points = sum([self.convert_points(question['answer']) for question in self.questions
                              if question['category'] == category])
            categories.append((Question.CATEGORY_MAPPINGS[category], sum_points))

        return sorted(categories, cmp=lambda x, y: cmp(x[1], y[1]), reverse=True)

    @classmethod
    def get_by_user_id(cls, user_id):
        """
        Get all quiz attempts from a user id
        :rtype: QuizAttempt or None
        """
        attempts = cls.query(cls.user_id == user_id).fetch()

        return attempts[0] if attempts else None

    @staticmethod
    def convert_points(answer):
        """
        Takes in the answer from the UI (0, 1, 2) and converts it to a
        point value (0, 2, 5) for calculation.
        """
        return [0, 2, 5][answer]
