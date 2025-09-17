def flatten(iterable):
    new = []
    for i in iterable:
        if isinstance(i, list):
            new.extend(flatten(i))
        elif i != None:
            new.append(i)
    return new
