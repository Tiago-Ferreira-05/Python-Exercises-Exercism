def is_isogram(string):
    string = "".join(ch for ch in string if ch not in " -")

    return len(string) == len(set(string.lower()))
