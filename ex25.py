def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    # .split() returns a list of all the words in the string , using ' ' as the separator
    return words


def sort_words(words):
    """Sorts the words"""
    # .sorted() returns a sorted list of the object
    return sorted(words)


def print_first_word(words):
    """Prints the first word after popping it off"""
    # .pop() removes an item at a specified index value from a list
    word = words.pop(0)
    print(word)


def print_last_word(words):
    """Prints the last word after popping it off"""
    # negative index number -1 refers to the last item
    word = words.pop(-1)
    print(word)


def sort_sentence(sentence):
    """Takes in a full sentence and returs the sorted words."""
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence):
    """Prints ths first and last words of the sentence"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentence):
    """Sorts the words the prints the first and last one"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
