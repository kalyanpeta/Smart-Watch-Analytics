from .config import SLEEP_QUESTIONS, RECOMMENDATIONS, STRESS_QUESTIONS, STRESS_RECOMMENDATIONS

def get_questions(category):
    """ Fetch questions based on the sleeper's category. """
    return SLEEP_QUESTIONS.get(category, [])

def get_recommendations(category, answers):
    """ Generate personalized recommendations based on the category and answers. """
    if all(answer.lower() == 'yes' for answer in answers):
        return RECOMMENDATIONS['yes'][category]
    else:
        return RECOMMENDATIONS['no'][category]

def get_stress_questions(stress_level):
    """ Fetch questions based on the stress level. """
    return STRESS_QUESTIONS.get(stress_level, [])

def get_stress_recommendations(stress_level, answers):
    """ Generate personalized recommendations based on the stress level and answers. """
    if all(answer.lower() == 'yes' for answer in answers):
        return STRESS_RECOMMENDATIONS['yes'][stress_level]
    else:
        return STRESS_RECOMMENDATIONS['no'][stress_level]
