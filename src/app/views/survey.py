"""
Survey view
"""

from . import TemplatedView

class IndexView(TemplatedView):

    def get(self):
        context = {
            'questions': [
                'Bunch',
                'Of',
                'Cool',
                'Q\'s',
            ]
        }

        self.render_response("showCategory.html", **context)
