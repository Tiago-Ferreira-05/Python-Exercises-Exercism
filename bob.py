def response(hey_bob):
    if hey_bob.strip() == "":
        return "Fine. Be that way!"
    
    question = is_question(hey_bob)
    yelling = is_yelling(hey_bob)

    if question and yelling:
        return "Calm down, I know what I'm doing!"
    elif question:
        return "Sure."
    elif yelling:
        return "Whoa, chill out!"
    else:
        return "Whatever."


def is_question(string):
    return string.rstrip().endswith("?")


def is_yelling(string):
    return string.isupper()

