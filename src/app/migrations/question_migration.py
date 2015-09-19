
from app.models.question import Question
from .keith_walker_gift_survey_questions import questions

category_mappings = {
    "adm": [1, 2, 21, 22, 41, 42, 61, 62, 81, 82],
    "apo": [3, 4, 23, 24, 43, 44, 63, 64, 83, 84],
    "cou": [5, 6, 25, 26, 45, 46, 65, 66, 85, 86],
    "dis": [7, 8, 27, 28, 47, 48, 67, 68, 87, 88],
    "eva": [9, 10, 29, 30, 49, 50, 69, 70, 89, 90],
    "fai": [11, 12, 31, 32, 51, 52, 71, 72, 91, 92],
    "giv": [13, 14, 33, 34, 53, 54, 73, 74, 93, 94],
    "hea": [15, 16, 35, 36, 55, 56, 75, 76, 95, 96],
    "int": [17, 18, 37, 38, 57, 58, 77, 78, 97, 98],
    "kno": [19, 20, 39, 40, 59, 60, 79, 80, 99, 100],
    "mir": [101, 102, 117, 118, 133, 134, 149, 150, 165, 166],
    "she": [103, 104, 119, 120, 135, 136, 151, 152, 167, 168],
    "pro": [105, 106, 121, 122, 137, 138, 153, 154, 169, 170],
    "ser": [107, 108, 123, 124, 139, 140, 155, 156, 171, 172],
    "sho": [109, 110, 125, 126, 141, 142, 157, 158, 173, 174],
    "tea": [111, 112, 127, 128, 143, 144, 159, 160, 175, 176],
    "ton": [113, 114, 129, 130, 145, 146, 161, 162, 177, 178],
    "wis": [115, 116, 131, 132, 147, 148, 163, 164, 179, 180],
}

def import_questions():
    for line in filter(lambda x: x != "", questions.splitlines()):
        # Split by the first period.
        question_number, text = line.split('.', 1)
        question_category = None
        for category in category_mappings:
            if int(question_number) in category_mappings[category]:
                question_category = category

        # Create the new question.
        question = Question()
        question.text = text.strip()
        question.category = question_category
        question.question_number = int(question_number.strip())
        question.put()
