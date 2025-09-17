"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 4


def bake_time_remaining(baked_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    remaining_bake_time = EXPECTED_BAKE_TIME - baked_time

    return remaining_bake_time


def preparation_time_in_minutes(number_of_layers=0):
    """Calculate the preparation time

    :param number_of_layers: int - number of layers of the lasagna
    :return: int - preparation time (in minutes)

    Function takes the number of layers of the lasagna and determines how long it will take 
    until the meal is prepared to go to the oven (assuming each layer takes 2 minutes to prepare).
    """

    time_per_layer = 2

    if number_of_layers != 0:
        preparation_time = time_per_layer * number_of_layers
    else:
        preparation_time = PREPARATION_TIME

    return preparation_time




def elapsed_time_in_minutes(number_of_layers=0, elapsed_bake_time=0):
    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """

    preparation_time = preparation_time_in_minutes(number_of_layers)
    total_cooking_time = preparation_time + elapsed_bake_time

    return total_cooking_time

