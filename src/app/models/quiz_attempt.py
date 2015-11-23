""" Quiz attempts model """
from google.appengine.ext import ndb

from .question import Question


class QuizAttemptAnswer(ndb.Model):
    """
    Model for use in QuizAttempt's StructuredProperty
    """
    question_number = ndb.IntegerProperty(required=True)
    category = ndb.StringProperty(required=True)
    answer = ndb.IntegerProperty()


class QuizAttempt(ndb.Model):
    """
    Stores information about a quiz attempt for a user.
    """
    user_id = ndb.IntegerProperty()
    questions = ndb.StructuredProperty(QuizAttemptAnswer, repeated=True)
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
            sum_points = sum([question.answer for question in self.questions
                              if question.category == category])
            categories.append((Question.CATEGORY_MAPPINGS[category], sum_points))

        return sorted(categories, cmp=lambda x, y: cmp(x[1], y[1]), reverse=True)

    @property
    def top_categories(self):
        """
        Top X categories. Just three for now, but acts strangely when there are ties.
        More succinctly: The top three can rotate right now, if there are ties.
        """
        return self.graded_categories[:3]

    @classmethod
    def get_by_user_id(cls, user_id):
        """
        Get first quiz attempt from a user id
        :param user_id: id of the user to get a quiz attempt for
        :rtype: QuizAttempt or None
        """
        if not user_id:
            raise ValueError('user_id must be provided')
        if type(user_id) != int:
            user_id = int(user_id)
        attempts = cls.query(cls.user_id == user_id).fetch()

        return attempts[0] if attempts else None
