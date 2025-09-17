BAND_COLORS = [
    "black", "brown", "red", "orange", "yellow",
    "green", "blue", "violet", "grey", "white"
]

PREFIX = {0: "", 3: "kilo", 6: "mega", 9: "giga"}

TOLERANCE = {
    "grey": "0.05%",
    "violet": "0.1%",
    "blue": "0.25%",
    "green": "0.5%",
    "brown": "1%",
    "red": "2%",
    "gold": "5%",
    "silver": "10%"}

def value(colors):
    if len(colors) == 1:
        return BAND_COLORS.index(*colors)
    elif len(colors) == 4:
        return int("".join(str(BAND_COLORS.index(c)) for c in colors[:2]))
    elif len(colors) == 5:
        return int("".join(str(BAND_COLORS.index(c)) for c in colors[:3]))
    

def resistor_label(colors):
    if len(colors) == 1:
        return f"{value(colors)} ohms"

    n = BAND_COLORS.index(colors[-2])

    result = value(colors) * (10**n)

    for key, p in PREFIX.items():
        if len(str(result // (10**key))) <= 3:
            final = result / (10**key)
            if final == int(final):
                final = int(final)
            prefix = p
            break

    for key in TOLERANCE:
        if key == colors[-1]:
            tolerance = TOLERANCE[key]

    return f"{final} {prefix}ohms ±{tolerance}"

