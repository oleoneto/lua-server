from datetime import date


SEASONS = {
    '3': 'Spring',
    '4': 'Spring',
    '5': 'Spring',
    '6': 'Summer',
    '7': 'Summer',
    '8': 'Summer',
    '9': 'Fall',
    '10': 'Fall',
    '11': 'Fall',
    '12': 'Winter',
    '1': 'Winter',
    '2': 'Winter',
}


def get_current_term():
    """
    Returns a string representation of the current season:
    Spring, Summer, Fall, Winter
    """
    today = date.today()
    return SEASONS[f'{today.month}']
