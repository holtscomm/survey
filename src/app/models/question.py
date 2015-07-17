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

    def get_pretty_category(self):
        """ Return the full (pretty) category name. """
        return self.CATEGORY_MAPPINGS[self.category]

    @classmethod
    def get_all_questions(cls):
        """ Returns all questions in a random order. """
        return cls.query().fetch(limit=180)
