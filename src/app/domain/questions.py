""" Domain code for questions """
from app.models.question import Question

QUESTIONS_PER_PAGE = 20


def get_survey_page(page_num):
    """
    Gets a page of the survey, based on the QUESTIONS_PER_PAGE variable.
    """
    if not page_num:
        raise ValueError('page_num is required')
    if page_num <= 0:
        raise ValueError('page_num must be 1 or higher')

    from_number = page_num * QUESTIONS_PER_PAGE if page_num > 1 else page_num
    to_number = (page_num + 1 if page_num > 1 else page_num) * QUESTIONS_PER_PAGE

    return Question.get_questions_by_number_range(from_number, to_number)
