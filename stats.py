from collections import defaultdict


def word_total(text):
    return text.lower().split()

def word_counts(text):
    words_list = word_total(text)
    words_dict = defaultdict(int)

    for w in words_list:
        words_dict[w] += 1

    return words_dict
