import random
from hiptr import Triptor, Diptor
import string
from bessemer import aesop

# TDL: get rid of .sample, fix up sweeper to not be twice as slow for no reason

class Mother:
    '''
    The doting mother of the family :)
    '''

    def __init__(self):
        self.storybook 
        self.daughter
    
    def open_storybook(self):
        self.storybook = [aesop()]
        
    def add_chapter(self, chapter):
        self.storybook.append(chapter)

    def bedtime_story(self, daughter):
        for chapter in self.storybook:
            self.daughter.listen(chapter)

        
class Daughter:
    '''
    What will she dream of?
    '''

    def __init__(self):
        self.memories = Diptor('Memories') # words_list[ ] diptor??
        self.memories[0,1] = '#START', '#END'
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
                
                remember(word_1, word_2)
                
    def remember(self, word_1, word_2):
        ndx1 = 0
        ndx2 = 0

        if word_1 in self.memories.dict:
            ndx1 = self.memories.dict[word_1]  # Triptor index
        else:
            self.memories.add(Triptor(word_1))

        if word_2 in self.memories.dict:
            ndx2 = self.memories.dict[word_2]  # Triptor index
        else:
            self.memories.add(Triptor(word_2))
        
        self.memories[ndx1].add(ndx2)

    def go_to_sleep(self):
        self.asleep = True
        self.dream()

    def dream(self): 
        thought = self.memories[0]  # Triptor! (start at starterchar)
        while self.asleep:                                                                             
            self.sleep_talk(thought.name)            
            wandering_memory = random.choices(thought.list, weights=thought.hist)
            thought = self.memories[wandering_memory]
            if thought == self.memories[1]:  # End at enderchar chosen
                wake_up()
                        
    def sleep_talk(self, babble):
        print(babble)

    def wake_up(self):
        self.asleep = False
    
if __name__ == "__main__":
    mom = Mother()
    mom.open_storybook()
    
