def rotate(text, key):
    cipher = ""

    for char in text:
        if char.islower():
            shifted = chr((ord(char) - ord('a') + key) % 26 + ord('a'))
        elif char.isupper():
            shifted = chr((ord(char) - ord('A') + key) % 26 + ord('A'))
        else:
            shifted = char  # leave digits, symbols, etc. unchanged

        cipher += shifted

    return cipher
