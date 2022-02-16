from dictogram import Dictogram
from handle_args import handle_args

class Markov():
    
    def __init__(self, source):
        self.chain = {}
        for i in range(len(source) - 1):
            word = source[i]
            next_word = source[i+1]
            if self.chain.get(word):
                self.chain[word].add_count(next_word)
            else:
                self.chain[word] = Dictogram([next_word])

                
    def get_next_word(self, word):
        found_hist = self.chain.get(word)
        if not found_hist:
            return None
        return found_hist.sample()
    
    def __str__(self) -> str:
        return str(self.chain)
                
def build_sentence(hist, markov, length=10):
    if length <= 0:
        return ""
    
    sentence = []
    current_word = hist.sample()
    sentence.append(current_word)
    new_word = None
    length -= 1
    for _ in range(length):
        
        new_word = markov.get_next_word(current_word)
        if not new_word:
            sentence.append(".")
            new_word = hist.sample()
        sentence.append(new_word)
        current_word = new_word
    
    ret_sentence = ""
    for word in sentence:
        ret_sentence += str(word) + ' '
    
    return ret_sentence

if __name__ == '__main__':
    settings = handle_args()
    source = settings.get('source_text')
    # print(source)
    hist = Dictogram(source)
    # print(hist)
    mark = Markov(source)
    # print(mark)
    sentence = build_sentence(hist, mark, 20)
    print(sentence)