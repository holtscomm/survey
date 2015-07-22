"""
Survey view
"""
import logging

from . import TemplatedView
from app.models.question import Question

class IndexView(TemplatedView):

    def get(self):
        context = {
            'questions': Question.get_all_questions(ordered=True)
        }

        logging.debug("%r", context['questions'])

        self.render_response("survey.html", **context)
