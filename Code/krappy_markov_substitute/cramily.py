import random
from hiptr import Triptor, Diptor, Hishtor, NormalHistogram
from arq import FixedQ
import string
from bessemer import aesop, clean
import cProfile
import re
import sys



# TDL: get rid of .sample, fix up sweeper to not be twice as slow for no reason

class Parent:
    '''
    The doting mother of the family :)
    '''

    def __init__(self):
        self.storybook = None
        self.child = None
    
    def open_storybook(self):
        self.storybook = [clean()]
        
    def add_chapter(self, chapter):
        self.storybook.append(chapter)

    def bedtime_story(self, child):
        for chapter in self.storybook:
            child.listen(chapter)

        
class Child:
    '''
    What will she dream of?
    '''

    def __init__(self):
        self.memories = Diptor('Memories') # words_list[ ] diptor??
        self.memories.add(NormalHistogram(' '.join(['#START']*int(sys.argv[2]))))
        self.memories.add(NormalHistogram('#END'))
        self.asleep = False

    def listen(self, chapter):  # boutta double these reads lol
        for sentence in chapter:
            n = int(sys.argv[2])
            qkey = FixedQ(n, ['#START']*n)
            word_2 = ''
            for place in range(len(sentence) + 1):
                if place == 0:
                    qkey.ndqueue('#START')
                else:
                    qkey.ndqueue(sentence[place - 1])

                if place == len(sentence):
                    word_2 = '#END'
                else:
                    word_2 = sentence[place]
                
                self.remember(str(qkey), word_2)
                
    def remember(self, word_1, word_2):
        ndx1 = -1
        ndx2 = -1

        if word_1 in self.memories.dict:
            ndx1 = self.memories.dict[word_1]  # Triptor index
        else:
            self.memories.add(NormalHistogram(word_1))
            ndx1 = len(self.memories.list) - 1

        if word_2 in self.memories.dict:
            ndx2 = self.memories.dict[word_2]  # Triptor index
        else:
            self.memories.add(NormalHistogram(word_2))
            ndx2 = len(self.memories.list) - 1

        self.memories.list[ndx1].add(ndx2)


    def go_to_sleep(self):
        self.asleep = True
        self.dream()

    def dream(self): 
        thought = self.memories.list[0]  # Hishtor! (start at starterchar) Panic!
        while self.asleep:                                                                             
            self.sleep_talk(thought.name)
            wandering_memory = thought.choice()
            # print(wandering_memory)
            thought = self.memories.list[wandering_memory] # why the zero? whatever, it works.
            if wandering_memory == '#END':  # End at enderchar chosen
                self.wake_up()
                        
    def sleep_talk(self, babble):
        if '#START' in babble:
            print(end=' ')
        else:
            print(babble, end=' ')

    def wake_up(self):
        self.asleep = False

def bedtime():
    mother = Parent()
    daughter = Child()
    mother.open_storybook()
    mother.bedtime_story(daughter)
    print('num is', end=': ')
    print(len(daughter.memories.list))
    # print(daughter.memories.list[3].name)
    # print(mother.storybook)

    print()
    print('TEXT PROCESSING COMPLETE')
    #for mem in daughter.memories.list:
    #    print(mem.list)
    loop = True
    while loop:
        count = input('enter a number of lines, or anything else to quit: ')
        if count.isnumeric():
            for i in range(int(count)):
                print()
                print([i], end=' ')
                daughter.go_to_sleep()
            print()
            print()
            #loop = False #rem
        else:
            loop = False



if __name__ == "__main__":
    cProfile.run('bedtime()')
    #bedtime()

    
