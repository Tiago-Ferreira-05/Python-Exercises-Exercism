PARTS = [
    "the house that Jack built.",
    "the malt that lay in the house that Jack built.",
    "the rat that ate the malt that lay in the house that Jack built.",
    "the cat that killed the rat that ate the malt that lay in the house that Jack built.",
    "the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
    "the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
    "the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
    "the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
    "the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
    "the rooster that crowed in the morn that woke the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
    "the farmer sowing his corn that kept the rooster that crowed in the morn that woke the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
    "the horse and the hound and the horn that belonged to the farmer sowing his corn that kept the rooster that crowed in the morn that woke the priest all shaven and shorn that married the man all tattered and torn that kissed the maiden all forlorn that milked the cow with the crumpled horn that tossed the dog that worried the cat that killed the rat that ate the malt that lay in the house that Jack built.",
]


def recite(start_verse, end_verse):
    """Return the verses from start_verse to end_verse inclusive.

    :param start_verse: int - index of first verse to include
    :param end_verse: int - index oflast verse to include
    :return: list[str] - verses in order, each starting with "This is ...".
    """
    return [f"This is {PARTS[i]}" for i in range(start_verse - 1, end_verse)]
