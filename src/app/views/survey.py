"""
Survey view
"""
import logging

from . import TemplatedView
from app.models.question import Question
from app.models.quiz_attempt import QuizAttempt


class IndexView(TemplatedView):
    """ Survey index """

    def get(self):
        """ GET """
        context = {
            'questions': Question.get_all_questions(ordered=True)[0:10]
        }

        logging.debug("%r", context['questions'])

        self.render_response("survey.html", **context)

    def post(self):
        """ POST """
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
