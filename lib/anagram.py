# your code goes here!


class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        anagram_words = []
        sotred_word = sorted([c for c in self.word])
        for word in word_list:
            if sorted([c for c in word]) == sotred_word:
                anagram_words.append(word)
        return anagram_words
