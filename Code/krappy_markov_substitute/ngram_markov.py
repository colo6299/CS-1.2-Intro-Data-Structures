import random
from arq import FixedQ
from hiptr import Diptor
from hiptr import NormalHistogram as Histogram
import string
from bessemer import aesop, clean
import cProfile
import re
import sys


# Well, fine. I'll do it right this time. 
class MarkovChain():
    def __init__(self):
        self.states = Diptor('States') # words_list[ ] diptor??
        self.states.add(Histogram(' '.join(['#START']*int(sys.argv[1]))))
        self.n = int(sys.argv[1])
        self.stopped = False
        self.corpus = []

        self.load_words()
        self.train()

    def load_words(self):
        self.corpus = clean()

    def train(self):  # boutta double these reads lol
        for sentence in self.corpus:
            sentence.extend(['#END'])
            qkey = FixedQ(self.n, ['#START']*self.n)
            for word in sentence:
                if str(qkey) in self.states.dict:
                    ndx1 = self.states.dict[str(qkey)]  # Triptor index
                else:
                    self.states.add(Histogram(str(qkey)))
                    ndx1 = len(self.states.list) - 1

                qkey.ndqueue(word)

                if str(qkey) in self.states.dict:
                    ndx2 = self.states.dict[str(qkey)]  # Triptor index
                else:
                    self.states.add(Histogram(str(qkey)))
                    ndx2 = len(self.states.list) - 1                 
                    
                self.states.list[ndx1].add(ndx2)
                #print('RATS!' + str(ndx1) + ' ' + str(ndx2))

    def generate(self):
        self.stopped = False
        state = self.states.list[0]
        while not self.stopped:
            choice_index = state.choice()
            state = self.states.list[choice_index]
            self.send(state.name.split(' ')[-1])

    def send(self, word):
        if word == '#END':
            self.stopped = True
            print()
            return
        print(word, end=' ')

    
if __name__ == "__main__":
    chain = MarkovChain()
    chain.train()
    print()
    print('TRAINING COMPLETE')
    print('WORD COUNT:', end=' ')
    print(len(chain.corpus))
    print()
    loop = True
    while loop:
        count = input('enter a number of lines, or anything else to quit: ')
        print()
        if count.isnumeric():
            for i in range(int(count)):
                
                print([i], end=' ')
                chain.generate()
            print()
            #loop = False #rem
        else:
            loop = False
        

        


                        
