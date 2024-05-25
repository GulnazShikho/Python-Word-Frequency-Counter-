from WordFrequencyCounter import count_words, top_words


def test_program(s: str):

    word_count = count_words(str1)

    print("\nTop 3 Most Frequent Words:")
    top_frequency_words = top_words(word_count, 3)
    for i, (word, freq) in enumerate(top_frequency_words, 1):
        print(f'{i}."{word}" - Frequency: {freq}')


if __name__ == "__main__":
    str1 = input("Enter a string: ")
    test_program(str1)