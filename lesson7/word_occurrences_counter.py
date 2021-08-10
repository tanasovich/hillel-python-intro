one_lined_string: str = input("Write one-lined string: ")

words: list = one_lined_string.split()

unique_words: set = set(words)

words_and_occur_numbers: dict = dict()

for word in unique_words:
    words_and_occur_numbers[word] = one_lined_string.count(word)

print(words_and_occur_numbers)
