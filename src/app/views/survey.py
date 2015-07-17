"""
Survey view
"""

from . import TemplatedView
from app.models.question import Question

class IndexView(TemplatedView):

    def get(self):
        context = {
            'questions': Question.get_all_questions()
        }

        self.render_response("showCategory.html", **context)
