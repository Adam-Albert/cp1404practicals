def main():
    """get some text and display the amount of times a word was used"""
    text = input("input string to count word occurrences\n>>>").split()
    words = count_occurrences(text)
    longest_word = get_longest_word(words)
    list_words(words, longest_word)


def get_longest_word(words):
    """get the longest word"""
    longest_word = ""
    for word in words.keys():
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word


def list_words(words, longest_word):
    """list words and values"""
    dict_items = sorted(words.items())
    for word, count in dict_items:
        print("{:{}} = {}".format(word, len(longest_word), count))


def count_occurrences(text):
    """count the occurrences of a word"""
    words = {}
    for word in text:
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1
    return words


if __name__ == '__main__':
    main()
