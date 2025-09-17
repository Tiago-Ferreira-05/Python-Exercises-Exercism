def square_of_sum(number):
    """Return the square of the sum of the first `number` natural numbers."""
    total = number * (number + 1) // 2  # Sum of first n natural numbers using Gauss' formula
    return total ** 2


def sum_of_squares(number):
    """Return the sum of the squares of the first `number` natural numbers."""
    return number * (number + 1) * (2 * number + 1) // 6  # Closed-form formula for sum of squares


def difference_of_squares(number):
    """Return the difference between square_of_sum and sum_of_squares."""
    return square_of_sum(number) - sum_of_squares(number)
