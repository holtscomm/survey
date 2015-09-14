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
        These are the final categories that someone is in. Unordered!

        Returns a dict like:
        {
            "adm": 10,
            "tea": 5,
            ...etc...
        }
        """
        categories = {q['category']: sum([self.convert_points(que['answer']) for que in self.questions if que['category'] == q['category']]) for q in self.questions}

        return categories

    @staticmethod
    def convert_points(answer):
        """
        Takes in the answer from the UI (0, 1, 2) and converts it to a
        point value (0, 2, 5) for calculation.
        """
        return [0, 2, 5][answer]
