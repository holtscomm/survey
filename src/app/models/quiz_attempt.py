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
    QUIZ_TYPES = {
        'fullform': 'Full',
        'short_a': 'Short A',
        'short_b': 'Short B',
        'trial': 'Trial'
    }

    user_id = ndb.StringProperty()
    questions = ndb.StructuredProperty(QuizAttemptAnswer, repeated=True)
    created = ndb.DateTimeProperty(auto_now_add=True)
    updated = ndb.DateTimeProperty(auto_now=True)
    quiz_type = ndb.StringProperty(default='fullform')

    @classmethod
    def build_key(cls, user_id, quiz_type='fullform'):
        """
        Build the key.
        :param user_id:
        :param quiz_type:
        :return:
        """
        return ndb.Key(cls, user_id + quiz_type)

    @classmethod
    def create(cls, user_id, quiz_type='fullform'):
        """
        Create a new quiz attempt and return the put entity.
        :param user_id:
        :param quiz_type:
        :return:
        """
        attempt_key = cls.build_key(user_id, quiz_type)
        attempt = QuizAttempt(
                key=attempt_key,
                user_id=user_id,
                quiz_type=quiz_type
        )
        attempt.put()

        return attempt

    @property
    def quiz_completed(self):
        return any([
            self.quiz_type in ['short_a', 'short_b'] and len(self.questions) == 90,
            self.quiz_type == 'fullform' and len(self.questions) == 180
        ])

    @property
    def quiz_link(self):
        return '/gifts/{}?userId={}'.format(
            '' if self.quiz_type == 'fullform' else 'trial/' if self.quiz_type == 'trial' else self.quiz_type.split('_')[1] + '/',
            self.user_id
        )

    @property
    def quiz_type_display(self):
        """
        Return the display version of the quiz type.
        :return:
        """
        return self.QUIZ_TYPES[self.quiz_type]

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
    def get_by_user_id(cls, user_id, quiz_type='fullform'):
        """
        Get first quiz attempt from a user id
        :param user_id: id of the user to get a quiz attempt for
        :param quiz_type: type of quiz
        :rtype: QuizAttempt or None
        """
        if not user_id:
            raise ValueError('user_id must be provided')
        if quiz_type not in cls.QUIZ_TYPES:
            raise ValueError('quiz_type must be one of {}'.format(cls.QUIZ_TYPES))

        return cls.build_key(user_id, quiz_type).get()

    @classmethod
    def get_all_attempts_for_user_id(cls, user_id):
        """
        Get all (up to three) attempts for the different quizzes.
        :param user_id:
        :return:
        """
        if not user_id:
            raise ValueError('user_id must be provided')

        return filter(None, [cls.get_by_user_id(user_id, quiz_type) for quiz_type in cls.QUIZ_TYPES.keys()])

    @classmethod
    def get_all_attempts(cls):
        return cls.query()

    @classmethod
    def get_non_trial_attempts(cls):
        return cls.get_all_attempts().filter(cls.quiz_type != 'trial')
