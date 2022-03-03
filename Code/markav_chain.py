from os import wait
from random import choice, random
from time import sleep
from dictogram import Dictogram
from handle_args import handle_args
from pprint import pprint
from make_tokens import get_tokens

class Markov():
    
    def __init__(self, source):
        self.chain = {}
        self.ends = []
        self.starts = []
        self.hist = Dictogram(source)
        
        for i in range(len(source) - 1):
            
            word = source[i]
            next_word = source[i+1]
            
            if self.chain.get(word):
                self.chain[word].add_count(next_word)
            else:
                self.chain[word] = Dictogram([next_word])
                
            if '.' in word:
                self.ends.append(word)
                self.starts.append(next_word)
                
    def get_next_word(self, word):
        found_hist = self.chain.get(word)
        if not found_hist:
            return None
        return found_hist.sample()
    
    def walk(self, length=30) -> str:
        words = []
        start = choice(self.starts)
        # print('got start:', start)
        # print('starts', self.starts, '\n')
        # print('ends', self.ends)
        
        current_word = self.get_next_word(start)
        while current_word not in self.ends and len(words) < length and current_word is not None:
            # print(current_word)
            words.append(current_word)
            current_word = self.get_next_word(current_word)
            
        return words
            
    
    def __str__(self) -> str:
        return str(self.chain)
           
class Markov2():
    
    def __init__(self, tokens) -> None:
        self.chain = {}
        self.ends = []
        self.starts = []
        self.hist = Dictogram()
        
        for i in range(len(tokens)-2):
            pair = (tokens[i], tokens[i+1])
            next_pair = (tokens[i+1], tokens[i+2])
            self.hist.add_count(pair)
            
            if pair in self.chain.keys():
                self.chain[pair].append(tokens[i+2])
            else:
                self.chain[pair] = [tokens[i+2]]
                
            if '.' in tokens[i+1]:
                self.starts.append(pair)
                self.ends.append(next_pair)
        
    
    def walk(self, length=10) -> str:
        words = []
        pairs = []
        start = self.hist.sample()
        
        current_pair = start
        while len(pairs) <= length and current_pair:
            pairs.append(current_pair)
            new_word = self.get_next_word(current_pair)
            new_pair = (current_pair[len(current_pair)-1], new_word)
            # print(current_pair, new_word, new_pair)
            current_pair = new_pair
            
        # pprint(pairs)
        
        for pair in pairs:
            if pair is not pairs[len(pairs)-1]:
                words.append(pair[1])
        
        # print(words)
        
        sentence = ''
        for word in words:
            sentence += word + ' '
        
        return sentence
    
    def get_next_word(self, pair):
        if pair not in self.chain.keys():
            return None
        choices = self.chain.get(pair)
        return choice(choices)
            

if __name__ == '__main__':
    settings = handle_args()
    # source = settings.get('source_text')
    source = get_tokens('data/script.txt')
    
    mark = Markov2(source)
    # print(mark.hist)
    sentence = mark.walk()
    
    print(sentence)