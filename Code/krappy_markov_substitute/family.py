import random
from hiptr import Triptor, Diptor
import string
from bessemer import aesop, clean

# TDL: get rid of .sample, fix up sweeper to not be twice as slow for no reason

class Mother:
    '''
    The doting mother of the family :)
    '''

    def __init__(self):
        self.storybook = None
        self.daughter = None
    
    def open_storybook(self):
        self.storybook = [clean()]
        
    def add_chapter(self, chapter):
        self.storybook.append(chapter)

    def bedtime_story(self, daughter):
        for chapter in self.storybook:
            daughter.listen(chapter)

        
class Daughter:
    '''
    What will she dream of?
    '''

    def __init__(self):
        self.memories = Diptor('Memories') # words_list[ ] diptor??
        self.memories.add(Triptor('#START'))
        self.memories.add(Triptor('#END'))
        self.asleep = False

    def listen(self, chapter):  # boutta double these reads lol
        for sentence in chapter:
            word_1 = ''
            word_2 = ''
            for place in range(len(sentence) + 1):
                if place == 0:
                    word_1 = '#START'
                else:
                    word_1 = sentence[place - 1]

                if place == len(sentence):
                    word_2 = '#END'
                else:
                    word_2 = sentence[place]
                
                self.remember(word_1, word_2)
                
    def remember(self, word_1, word_2):
        ndx1 = -1
        ndx2 = -1

        if word_1 in self.memories.dict:
            ndx1 = self.memories.dict[word_1]  # Triptor index
        else:
            self.memories.add(Triptor(word_1))
            ndx1 = len(self.memories.list) - 1

        if word_2 in self.memories.dict:
            ndx2 = self.memories.dict[word_2]  # Triptor index
        else:
            self.memories.add(Triptor(word_2))
            ndx2 = len(self.memories.list) - 1

        self.memories.list[ndx1].add(ndx2)
        

    def go_to_sleep(self):
        self.asleep = True
        self.dream()

    def dream(self): 
        thought = self.memories.list[0]  # Triptor! (start at starterchar)
        while self.asleep:                                                                             
            self.sleep_talk(thought.name)
            wandering_memory = random.choices(thought.list, weights=thought.hist)
            # print(wandering_memory)
            thought = self.memories.list[wandering_memory[0]] # why the zero? whatever, it works.
            if thought == self.memories.list[1]:  # End at enderchar chosen
                self.wake_up()
                        
    def sleep_talk(self, babble):
        if babble == '#START':
            print(end=' ')
        else:
            print(babble, end=' ')

    def wake_up(self):
        self.asleep = False
        
    
if __name__ == "__main__":
    mother = Mother()
    daughter = Daughter()
    mother.open_storybook()
    mother.bedtime_story(daughter)
    
    # print(daughter.memories.list[3].name)
    # print(mother.storybook)

    print()
    print('TEXT PROCESSING COMPLETE')
    loop = True
    while loop:
        count = input('enter a number of lines, or anyhting else to quit: ')
        if count.isnumeric():
            for i in range(int(count)):
                print()
                print([i], end=' ')
                daughter.go_to_sleep()
            print()
            print()
        else:
            loop = False

    
