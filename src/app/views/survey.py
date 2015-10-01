"""
Survey view
"""
from . import TemplatedView
from app.domain.questions import get_survey_page
from app.models.quiz_attempt import QuizAttempt


class SurveyView(TemplatedView):
    """ Survey index """

    def get(self):
        """ GET """
        context = {
            'questions': None  # Eventually maybe this can be server-side-generated React?
        }

        self.render_response("survey.html", **context)

    def post(self):
        """ POST """
        # TODO: Move all of this into domain layer
        question_list = []
        for i in range(1, 11):
            question_list.append({
                'question_number': int(self.request.get('question-number-{}'.format(i), 0)),
                'category': self.request.get('question-category-{}'.format(i)),
                'answer': int(self.request.get('choice{}'.format(i), 0)),
            })

        quiz_attempt = QuizAttempt(user_id=1, questions=question_list)
        quiz_attempt.put()
        self.redirect('/')
