def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    
    factor = 1
    aliquot_sum = 0

    while factor < number:
        if not (number % factor):
            aliquot_sum += factor
        factor += 1

    classification = {"perfect": number == aliquot_sum, "abundant": number < aliquot_sum, "deficient": number > aliquot_sum}

    for key, value in classification.items():
        if value:
            return key
