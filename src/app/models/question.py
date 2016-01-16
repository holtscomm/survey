"""
Question model
"""
from google.appengine.ext import ndb


class Question(ndb.Model):

    text = ndb.TextProperty()
    category = ndb.StringProperty()
    question_number = ndb.IntegerProperty()

    CATEGORY_MAPPINGS = {
        "adm": "Administration (Leadership)",
        "apo": "Apostleship (Missionary)",
        "cou": "Counsellor (Exhorter)",
        "dis": "Discernment",
        "eva": "Evangelist",
        "fai": "Faith",
        "giv": "Giving",
        "hea": "Healing",
        "int": "Interpretation of Tongues",
        "kno": "Knowledge",
        "mir": "Miracles",
        "pro": "Prophecy (Preacher/Proclaimer)",
        "she": "Sheperding (Pastor/Teacher)",
        "ser": "Serving (Helps)",
        "sho": "Showing Mercy (Compassion)",
        "tea": "Teaching",
        "ton": "Tongues",
        "wis": "Wisdom"
    }

    @classmethod
    def build_key(cls, question_number):
        """
        Build a key for a new Question.
        :param question_number:
        :return:
        """
        return ndb.Key(cls, question_number)

    @classmethod
    def create(cls, text, category, question_number):
        """
        Create a new question.
        :param text:
        :param category:
        :param question_number:
        :return:
        """
        question = Question(
            key=cls.build_key(question_number),
            text=text,
            category=category,
            question_number=question_number
        )
        question.put()

    @property
    def pretty_category(self):
        """ Return the full (pretty) category name. """
        return self.CATEGORY_MAPPINGS[self.category]

    @classmethod
    def get_all_questions(cls, ordered=False, limit=180):
        """ Returns all questions in a random order. """
        if ordered:
            return cls.query().order(cls.question_number).fetch(limit=limit)

        return cls.query().fetch(limit=limit)

    @classmethod
    def get_by_question_number(cls, question_number):
        """
        Get a question by question number (i.e. 3)
        :param question_number:
        :return:
        """
        return cls.build_key(question_number).get()

    @classmethod
    def get_questions_by_number_range(cls, from_number, to_number):
        """ Gets questions by a range of question_numbers (21 - 40). Returned in ascending order. """
        if not from_number:
            raise ValueError('from_number is required')
        if not to_number:
            raise ValueError('to_number is required')

        return cls.query(cls.question_number >= from_number, cls.question_number <= to_number)\
            .order(cls.question_number).fetch()
