def is_triangle(sides):
    a, b, c = sides

    if a + b >= c and b + c >= a and a + c >= b and (a and b and c):
        return True
    return False

def equilateral(sides):
    if is_triangle(sides):
        a, b, c = sides
        return a == b == c
    return False 


def isosceles(sides):
    if is_triangle(sides):
        a, b, c = sides
        return a == b or a == c or b == c
    return False


def scalene(sides):
    if is_triangle(sides):
        a, b, c = sides
        return a != b and a != c and b != c
    return False

#Great solution using decorators:
"""
def valid_triangle(f):
    def inner(sides):
        return sum(sides) > 2 * max(sides) and f(sides)
    return inner


@valid_triangle
def equilateral(sides):
    return len(set(sides)) == 1


@valid_triangle
def isosceles(sides):
    return len(set(sides)) < 3


@valid_triangle
def scalene(sides):
    return len(set(sides)) == 3



Chat GPT version of my code:

def is_triangle(sides):
    a, b, c = sorted(sides)
    return a > 0 and a + b > c  # Sorting makes this check simpler

def equilateral(sides):
    return is_triangle(sides) and len(set(sides)) == 1

def isosceles(sides):
    return is_triangle(sides) and len(set(sides)) <= 2

def scalene(sides):
    return is_triangle(sides) and len(set(sides)) == 3

"""