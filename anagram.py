def find_anagrams(word, candidates):
    """Find anagrams of a given word inside candidates

    :param word: str - the word from which anagrams are being discovered
    :param candidates: list[str] - list of candidate words as anagrams
    :return: list[str] - elements of candidates which are an anagram of word
    """

    anagrams = []
    word = word.lower()
    sorted_word = "".join(sorted(word))

    for x in candidates:
        lower_x = x.lower()
        sorted_x = "".join(sorted(lower_x))
        if sorted_x == sorted_word and lower_x != word:
            anagrams.append(x)

    return anagrams
