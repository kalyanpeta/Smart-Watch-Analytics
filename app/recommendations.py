from .config import SLEEP_QUESTIONS, RECOMMENDATIONS

def get_questions(category):
    """ Fetch questions based on the sleeper's category. """
    return SLEEP_QUESTIONS.get(category, [])

def get_recommendations(category, answers):
    """ Generate personalized recommendations based on the category and answers. """
    if all(answer.lower() == 'yes' for answer in answers):
        return RECOMMENDATIONS['yes'][category]
    else:
        return RECOMMENDATIONS['no'][category]
