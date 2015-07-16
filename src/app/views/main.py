"""
Main view
"""

from . import TemplatedView

class MainView(TemplatedView):

    def get(self):
        self.render_response("index.html")
