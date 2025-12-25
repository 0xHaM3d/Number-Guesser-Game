import random

def generate_random_number(start: int, end: int) -> int:
    """generate a darnom number between 1 and 100

    Args:
        start (_type_): _description_
        end (_type_): _description_
    """
    return random.randint(start, end)