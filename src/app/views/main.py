"""
Main view
"""

from app.views import TemplatedView

class MainView(TemplatedView):

    def get(self):
        self.render_response("index.html")
