# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = sorted([char for char in word])
        
    def match(self, word_list):
        pair = [wrd for wrd in word_list if sorted([char for char in wrd]) == self.word]
        return pair