"""Pizza preparation functions"""
EXPECTED_BAKE_TIME = 40


def bake_time_remaining(elapsed_bake_time):
    """Calculate remaining bake time"""
    return EXPECTED_BAKE_TIME - elapsed_bake_time
    

def preparation_time_in_minutes(number_of_layers):
    """Calculate how much time is need to prepare all layers"""
    return number_of_layers * 2


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate sum of the needed time for baking and preparation"""
    total = number_of_layers*2 + elapsed_bake_time
    return total
