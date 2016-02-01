""" Question domain object """
from app.models.question import Question
from app.models.quiz_attempt import QuizAttempt

QUESTIONS_PER_PAGE = 15


def survey_for_type(quiz_type='fullform'):
    """
    Helper function that returns a survey object for the quiz_type passed in.
    :param quiz_type:
    :return:
    """
    if quiz_type == 'short_a':
        return ShortASurvey
    elif quiz_type == 'short_b':
        return ShortBSurvey
    elif quiz_type == 'trial':
        return TrialSurvey
    else:
        return Survey


class Survey(object):
    """
    Base Survey object. Has 180 questions, as opposed to the shorter ones which have 90.
    """
    def __init__(self, user_id, quiz_type='fullform', max_pages=12):
        if not user_id:
            raise ValueError('user_id is required')
        self.user_id = user_id
        self.quiz_type = quiz_type
        self.max_pages = max_pages

    @property
    def first_page(self):
        """
        Gets the first page a user id needs to start on. If they haven't answered any questions or up to
        20 questions, that's page 1. If they've answered 21-40 questions, that's page 2, and so on.
        """
        quiz_attempt = QuizAttempt.get_by_user_id(self.user_id, self.quiz_type)

        return (len(quiz_attempt.questions) / QUESTIONS_PER_PAGE) + 1

    def get_survey_page(self, page_num):
        """
        Get information about a page of the survey. Specifically:

        - The questions for that page
        - The previous page number
        - The next page number, or False if there are no more pages.

        :param page_num:
        """
        survey_page = self._get_questions_for_survey_page(page_num)

        questions = [{
            "question_number": question.question_number,
            "text": question.text,
            "answer": None,
            "category": question.category
        } for question in survey_page]

        questions = self._normalize_question_numbers(questions, page_num, out=True)

        prev_page = 1 if page_num == 1 else page_num - 1
        next_page = False if page_num >= self.max_pages else page_num + 1

        return questions, prev_page, next_page

    def save_user_submitted_answers(self, submitted):
        """
        Save answers submitted to the API.
        :param submitted:
        """
        quiz_attempt = QuizAttempt.get_by_user_id(self.user_id, self.quiz_type)

        if type(submitted) == list and len(submitted) > 0:
            questions_start = submitted[0].question_number - 1
            questions_end = submitted[-1].question_number
        else:
            return

        page_num = (questions_start / QUESTIONS_PER_PAGE) + 1
        submitted = self._normalize_question_numbers(submitted, page_num, out=False)

        for question in quiz_attempt.questions[questions_start:questions_end]:
            if question.question_number == submitted[0].question_number:
                quiz_attempt.questions[question.question_number - 1].answer = submitted.pop(0).answer

        quiz_attempt.questions.extend(submitted)
        quiz_attempt.put()

    def _get_questions_for_survey_page(self, page_num):
        """
        Gets a page of the survey.
        """
        if not page_num:
            raise ValueError('page_num is required')
        if type(page_num) != int:
            page_num = int(page_num)
        if page_num <= 0:
            raise ValueError('page_num must be 1 or higher')

        from_number, to_number = self._calculate_from_and_to_for_page_number(page_num)

        return Question.get_questions_by_number_range(from_number, to_number)

    @staticmethod
    def _calculate_from_and_to_for_page_number(page_num):
        """
        Calculate the question numbers of a page of the survey, based on the QUESTIONS_PER_PAGE variable.
        """
        from_number = ((page_num - 1) * QUESTIONS_PER_PAGE) + 1 if page_num > 1 else page_num
        to_number = page_num * QUESTIONS_PER_PAGE

        return from_number, to_number

    def _normalize_question_numbers(self, questions, page_num, out=True):
        """
        Convert short question numbers to regular numbers, or vice versa.
        :param questions:
        :param page_num:
        :param out:
        :return:
        """
        return questions


class ShortASurvey(Survey):
    QUESTIONS = [
        2, 5, 8, 10, 13, 20, 22, 23, 25, 28, 30, 31, 32, 34, 35, 38, 40, 43, 45, 48, 50, 52,
        53, 54, 56, 57, 60, 61, 62, 63, 64, 65, 68, 70, 71, 74, 75, 76, 77, 79, 80, 82, 83,
        86, 88, 89, 91, 96, 97, 98, 101, 104, 106, 110, 112, 114, 118, 120, 123, 126, 127,
        130, 132, 134, 136, 137, 138, 139, 140, 142, 143, 146, 147, 148, 149, 152, 153, 155,
        157, 160, 161, 163, 166, 167, 169, 171, 174, 176, 178, 180
    ]

    def __init__(self, user_id, quiz_type='short_a'):
        """
        :param user_id:
        :param quiz_type:
        :return:
        """
        max_pages = len(self.QUESTIONS) / QUESTIONS_PER_PAGE
        super(ShortASurvey, self).__init__(user_id, quiz_type=quiz_type, max_pages=max_pages)

    def _normalize_question_numbers(self, questions, page_num, out=True):
        """
        Convert short question numbers to regular numbers, or vice versa.
        :param questions:
        :param page_num:
        :param out:
        :return:
        """
        if len(questions) == 0:
            return questions

        from_num, to_num = self._calculate_from_and_to_for_page_number(page_num)
        index = 0
        for new_question_number in range(from_num, to_num + 1):
            if not out:
                # The questions come in as QuizAttemptAnswers so we have to access their attribute.
                questions[index].question_number = self.QUESTIONS[new_question_number - 1]
            else:
                # The questions go out as regular dictionaries to we have to set the index.
                questions[index]['question_number'] = new_question_number
            index += 1

        return questions

    def _get_questions_for_survey_page(self, page_num):
        from_num, to_num = self._calculate_from_and_to_for_page_number(page_num)

        questions = self.QUESTIONS[from_num - 1:to_num]
        return [Question.get_by_question_number(q_num) for q_num in questions]


class ShortBSurvey(ShortASurvey):
    QUESTIONS = [
        1, 3, 4, 6, 7, 9, 11, 12, 14, 15, 16, 17, 18, 19, 21, 24, 26, 27, 29, 33, 36, 37,
        39, 41, 42, 44, 46, 47, 49, 51, 55, 58, 59, 66, 67, 69, 72, 73, 78, 81, 84, 85, 87,
        90, 92, 93, 94, 95, 99, 100, 102, 103, 105, 107, 108, 109, 111, 113, 115, 116, 117,
        119, 121, 122, 124, 125, 128, 129, 131, 133, 135, 141, 144, 145, 150, 151, 154, 156,
        158, 159, 162, 164, 165, 168, 170, 172, 173, 175, 177, 179
    ]

    def __init__(self, user_id, quiz_type='short_b'):
        """
        :param user_id:
        :param quiz_type:
        :return:
        """
        super(ShortBSurvey, self).__init__(user_id, quiz_type=quiz_type)


class TrialSurvey(ShortBSurvey):
    QUESTIONS = [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15
    ]

    def __init__(self, user_id, quiz_type='trial'):
        """
        :param user_id:
        :param quiz_type:
        :return:
        """
        super(TrialSurvey, self).__init__(user_id, quiz_type=quiz_type)
