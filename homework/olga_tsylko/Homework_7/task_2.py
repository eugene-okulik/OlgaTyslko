words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}


def print_dicts(words):
    for key, value in words.items():
        print(key * value)


print_dicts(words)
