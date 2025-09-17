def find(search_list, value):
    #lo = lower index of list
    #hi = higher index of list
    def helper(lo, hi):
        if lo > hi:
            raise ValueError("value not in array")

        mid = (lo + hi) // 2

        if search_list[mid] == value:
            return mid
        elif search_list[mid] < value:
            return helper(mid + 1, hi)
        else:
            return helper(lo, mid - 1)

    return helper(0, len(search_list) - 1)
