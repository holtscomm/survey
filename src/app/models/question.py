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
    def get_questions_by_number_range(cls, from_number, to_number):
        """ Gets questions by a range of question_numbers (21 - 40). Returned in ascending order. """
        if not from_number:
            raise ValueError('from_number is required')
        if not to_number:
            raise ValueError('to_number is required')

        return cls.query(cls.question_number >= from_number, cls.question_number <= to_number)\
            .order(cls.question_number).fetch()
