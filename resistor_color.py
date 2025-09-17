# List of resistor colors in order
BAND_COLORS = [
    "black", "brown", "red", "orange", "yellow",
    "green", "blue", "violet", "grey", "white"
]

def color_code(color):
    """Return the numeric value associated with a resistor color.
    
    :param color: str - color name.
    :return: int - numeric value of the color (0-9).
    """
    
    return BAND_COLORS.index(color)

def colors():
    """Return a list of all resistor colors in order.
    
    :return: list[str] - all resistor colors from black to white.
    """

    return BAND_COLORS.copy()
