def square(number):
    if not (1 <= number <= 64): 
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number-1)

"""
My solution:
def total():
    total = 0
    for i in range(0, 64):
        total += 2 ** i
    
    return total
"""
def total():
    return 2**64 -1
