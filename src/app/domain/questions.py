""" Domain code for questions """
from app.models.question import Question
from app.models.quiz_attempt import QuizAttempt
from app.utils import list_get_or_default

QUESTIONS_PER_PAGE = 20


def save_user_submitted_answers(user_id, submitted):
    """
    Save answers submitted to the API.
    """
    quiz_attempt = QuizAttempt.get_by_user_id(user_id)

    if type(submitted) == list and len(submitted) > 0:
        questions_start = submitted[0]['question_number'] - 1
    else:
        questions_start = 0

    for question in quiz_attempt.questions[questions_start:len(submitted)]:
        quiz_attempt.questions[question['question_number'] - 1]['answer'] = submitted.pop(0)['answer']

    quiz_attempt.questions.extend(submitted)
    quiz_attempt.put()


def get_survey_page(page_num):
    """
    Gets a page of the survey.
    """
    if not page_num:
        raise ValueError('page_num is required')
    if type(page_num) != int:
        page_num = int(page_num)
    if page_num <= 0:
        raise ValueError('page_num must be 1 or higher')

    from_number, to_number = _calculate_from_and_to_for_page_number(page_num)

    return Question.get_questions_by_number_range(from_number, to_number)


def get_survey_page_for_user_id(page_num, user_id):
    """
    Gets a page of the survey and fills in a user's answers on it in the event it has already been filled out.
    """
    survey_page = get_survey_page(page_num)
    try:
        user_attempt = QuizAttempt.get_by_user_id(user_id)
        user_answers = user_attempt.questions
    except AttributeError:
        user_answers = []

    questions = []
    # Rectify the page with the user's answers and return a list.
    for question in survey_page:
        questions.append({
            "question_number": question.question_number,
            "text": question.text,
            "answer": list_get_or_default(user_answers, question.question_number - 1, {}).get('answer', None),
            "category": question.category
        })

    prev_page = 1 if page_num == 1 else page_num - 1
    next_page = False if page_num == 9 else page_num + 1

    return questions, prev_page, next_page


def _calculate_from_and_to_for_page_number(page_num):
    """
    Calculate the question numbers of a page of the survey, based on the QUESTIONS_PER_PAGE variable.
    """
    from_number = ((page_num - 1) * QUESTIONS_PER_PAGE) + 1 if page_num > 1 else page_num
    to_number = page_num * QUESTIONS_PER_PAGE

    return from_number, to_number
