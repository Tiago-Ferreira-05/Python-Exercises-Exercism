def append(list1, list2):
    list1 = [*list1, *list2]

    return list1


def concat(lists):
    new_list = []

    for item in lists:
        new_list += item

    return new_list


def filter(function, list):
    new_list = []

    for item in list:
        if function(item):
            new_list = append(new_list, [item])

    return new_list


def length(list):
    count = 0

    for _ in list:
        count += 1

    return count


def map(function, list):
    new_list = []

    for item in list:
        new_list = append(new_list, [function(item)])

    return new_list


def foldl(function, list, accumulator):
    for item in list:
        accumulator = function(accumulator, item)

    return accumulator

def foldr(function, list, accumulator):
    new_list = list[::-1]
    for item in new_list:
        accumulator = function(accumulator, item)

    return accumulator


def reverse(list):
    new_list = list[::-1]
    return new_list
