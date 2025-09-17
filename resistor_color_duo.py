# List of resistor colors in order
BAND_COLORS = [
    "black", "brown", "red", "orange", "yellow",
    "green", "blue", "violet", "grey", "white"
]

def value(colors):
    """Return the numeric value of the first two color bands.
    
    :param colors: list[str] - list of resistor colors.
    :return: int - two-digit number representing the first two bands.
    """
    # Take first two colors, look up their indices, join into a string, convert to int
    return int("".join(str(BAND_COLORS.index(c)) for c in colors[:2]))
