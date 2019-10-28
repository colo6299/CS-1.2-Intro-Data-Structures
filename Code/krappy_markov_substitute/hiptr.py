import random
import math

class Diptor:

    def __init__(self, name = 'None'):
        self.name = name
        self.list = []
        self.dict = {}

    def add(self, item):
        '''
        Adds item to diptor

        Item must have hashable name property!
        '''
        self.list.append(item)
        self.dict[item.name] = len(self.list) - 1



class Triptor:
    '''
    '''

    def __init__(self, name = 'None'):
        self.name = name
        self.list = []
        self.hist = []
        self.dict = {}

    def add(self, item):
        '''
        Adds item to triptor

        Item must be hashable! 
        '''
        if item in self.dict:
            ndx = self.dict[item]       
            self.hist[ndx] += 1
        else:
            self.list.append(item)
            self.hist.append(1)
            self.dict[item] = len(self.list) - 1
        
    def remove(self, item):
        '''
        Lookup is fast, probably

        Returns true if object 'item' was found and removed from the Triptor. 

        Returns false if object 'item' was not removed. (not in list, or 0 in hist)
        '''
        if item in self.dict:
            ndx = self.dict[item]
            if hist[ndx] < 1:
                self.hist[ndx] = 0
                return False
            else:
                self.hist[ndx] -= 1
                return True
        else:
            return False


class Hishtor:
    '''
    uhhhhhhh

    Can we just agree this thing runs on witchcraft? 
    '''

    def __init__(self, name = 'None'):
        self.name = name
        self.addchance = 1
        self.domain = 0
        self.fresh = False
        self.total = 0
        self.list = []
        self.dict = {}

    def add(self, item):
        '''
        Adds item to hishtor

        Item must be an int? maybe just hashable? I don't know! 
        '''
        if item in self.dict:
            ndx = self.dict[item]     
            self.total += 1
            self.addchance = len(self.list) / self.total
            if ndx != 0 and random.random() < self.addchance:   
                swp = self.list[ndx - 1]
                self.dict[swp] += 1
                self.dict[item] -= 1
                self.list[ndx] = swp
                self.list[ndx - 1] = item

        else:
            self.list.append(item)
            self.total += 1
            self.dict[item] = len(self.list) - 1
        
    def remove(self, item):
        '''
        Lookup is fast, probably

        Returns true if object 'item' was found and removed from the Hishtor. 

        Returns false if object 'item' was not removed. (not in list, or 0 in hist)

        Bonus: it doesn't work at all. Avoid at all costs.
        '''
        if item in self.dict:
            ndx = self.dict[item]
            if hist[ndx] < 1:
                self.hist[ndx] = 0
                return False
            else:
                self.hist[ndx] -= 1
                return True
        else:
            return False

    def choice(self):
        '''
        This is just running a simple hard-coded e^kx

        don't expect it to model things well lmao
        '''
        if not self.fresh:
            self.domain = math.log(len(self.list)) / 0.05
        
        index = int(math.exp(self.domain * random.random() * 0.05))
        return self.list[index - 1]  # ...yeah I tacked on a (-1) and it started working



def test_triptor():
    triptor = Triptor('The')
    triptor.add(1)
    triptor.add(3)
    triptor.add(7)
    triptor.add(1)

    assert triptor.hist[0] == 2
