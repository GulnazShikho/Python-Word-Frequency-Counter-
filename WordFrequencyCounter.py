from operator import itemgetter
import string


def count_words(s: str) -> dict:
    """
    a function that takes a string and returns a dictionary that maps each word to its frequency.
    :param s: input string
    :return: dictionary that maps each word to its frequency.
    """

    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = s.translate(translator).lower().strip()

    lst1 = cleaned_text.split()

    word_freq = {}
    for word in lst1:
        word_freq[word] = word_freq.get(word, 0) + 1

    return word_freq


def top_words(d: dict, n = 3) -> list:
    """
     a function that takes a dictionary and Sort it by values in descending order and return the top N.
    :param d:  dictionary
    :param n: number of top values to display
    :return: a list that holds the top N words frequency along with their frequencies in descending order.
    """
    top_n = sorted(d.items(), key=itemgetter(1), reverse=True)[:n]
    return top_n

