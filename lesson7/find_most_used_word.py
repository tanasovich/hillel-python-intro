multi_lined_string: str = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur facilisis enim quis auctor vulputate.
Vestibulum sed varius felis.
Duis lobortis ante vitae nisi condimentum ornare.
Donec fringilla egestas tempor.
Donec interdum nisl massa, sit amet consectetur massa eleifend nec.
Mauris eros arcu, commodo a mi ut, rhoncus porttitor urna.
Aliquam dictum rutrum congue.
'''

words: list = multi_lined_string.split()

unique_words: set = set(words)

words_and_occur_numbers: dict = dict()

for word in unique_words:
    words_and_occur_numbers[word] = words.count(word)

print(sorted([(count, word) for word, count in words_and_occur_numbers.items()]).pop()[1])
