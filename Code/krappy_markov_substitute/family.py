import random
from hiptr import Triptor

class Mother:
    '''
    The doting mother of the family :)
    '''

    def __init__(self):
        pass
    
    def open_storybook(self):
        f = open('aesop.txt', 'r')
        words_list = f.readlines()
        f.close()
        # print(words_list)
        # words_list = words_list[0].split('\n')
        s_prune = []
        # print(words_list)
        for i in range(len(words_list)):
            if len(words_list[i]) < 80:
                s_prune.append(i) 

        s_prune.reverse()
        for i in s_prune:
            words_list.pop(i)
        print(words_list)

    def bedtime_story(self, daughter):
        open_storybook()

        
class Daughter:
    '''
    What will she dream of?
    '''

    def __init__(self):
        self.memories = [] # words_list[ ] diptor??
        self.asleep = False

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
        


