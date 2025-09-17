def is_armstrong_number(number):
    """Determine if a number is an Amstrong number

    :param number: int - some number
    :return: bool - return True if the number is an Amstrong number

    Example:
    - 153 is an Armstrong number, because: `153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153`
    - 154 is _not_ an Armstrong number, because: `154 != 1^3 + 5^3 + 4^3 = 1 + 125 + 64 = 190` 
    
    """
    str_number = str(number)
    number_of_digits = len(str_number)
    result = 0

    for i in range(0, number_of_digits):
        result += int(str_number[i])**number_of_digits

    return result == number
