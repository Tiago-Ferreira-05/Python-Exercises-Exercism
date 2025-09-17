def convert(number):
    """Convert a number into a raindrop sound string based on its factors

    For each factor of the number:
    - 3 adds "Pling"
    - 5 adds "Plang"
    - 7 adds "Plong"

    If the number has none of these factors, return the number itself as a string.

    :param number: int - the number to convert.
    :return: str - the resulting raindrop string or the number itself if no factors match.
    """

    rain = ""

    divisible_by_3 = number % 3
    divisible_by_5 = number % 5
    divisible_by_7 = number % 7

    if divisible_by_3 == 0:
        rain += "Pling"
    if divisible_by_5 == 0:
        rain += "Plang"
    if divisible_by_7 == 0:
        rain += "Plong"
    if rain == "":
        rain = str(number)
    
    return rain
