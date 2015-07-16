"""
Question model
"""
from google.appengine.ext import ndb

class Question(ndb.Model):

    text = ndb.TextProperty()
    category = ndb.StringProperty()
    

    @staticmethod
    def get_category_mappings():
        return {
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
