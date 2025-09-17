def is_valid(isbn):
    digits = []
    total = 0
    n = 10

    for idx, char in enumerate(isbn):
        if char.isnumeric():
            digits.append(int(char))
        elif char == 'X' and idx == len(isbn) - 1:
            digits.append(10)
        elif char != "-":
            return False

    if len(digits) != 10:
        return False

    for digit in digits:
        total += digit * n
        n -= 1

    return total % 11 == 0
