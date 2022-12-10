import random


class StartGame:
    def __init__(self, word_list):
        if word_list == '':
            raise ValueError('word_list cannot be empty')
        self.word_list = word_list
        self.shuffled_word_list = self.shuffle_words()

    def shuffle_words(self):
        shuffled_word = []
        for word in self.word_list:
            str = ''.join(random.sample(word, len(word)))
            shuffled_word.append(str)
        return shuffled_word