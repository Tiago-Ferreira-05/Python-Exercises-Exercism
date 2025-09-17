BAND_COLORS = [
    "black", "brown", "red", "orange", "yellow",
    "green", "blue", "violet", "grey", "white"
]

PREFIX = {0: "", 3: "kilo", 6: "mega", 9: "giga"}


def value(colors):
    """Return the numeric value of the first two color bands.
    
    :param colors: list[str] - list of resistor colors.
    :return: int - two-digit number representing the first two bands.
    """
    return int("".join(str(BAND_COLORS.index(c)) for c in colors[:2]))


def label(colors):
    n = BAND_COLORS.index(colors[-2])

    result = value(colors) * (10**n)

    for key, p in PREFIX.items():
        if len(str(result // (10**key))) <= 3:
            final = result // (10**key)
            prefix = p
            break

    return f"{final} {prefix}ohms"
