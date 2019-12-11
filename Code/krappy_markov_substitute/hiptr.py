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

    def choice(self, blah=0, blaw=1):
        return random.choices(self.list, self.hist)


class Hishtor:
    '''
    uhhhhhhh

    Can we just agree this thing runs on witchcraft? 
    '''

    def __init__(self, name = 'None', k_value = 1):
        self.name = name
        self.k_value = k_value
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
            self.domain = math.log(len(self.list) + 1) * self.k_value
        
        index = int(math.exp(self.domain * random.random() / self.k_value))
        return self.list[index - 1]  # ...yeah I tacked on a (-1) and it started working



class NormalHistogram:
    '''
    Nothing strange here whatsoever.
    '''

    def __init__(self, name = 'None'):
        self.name = name  # just in case you want to give your pet histogram a name :)
        self.list_of_items = []
        self.count_of_items = []
        self.normal_chance = []
        self.sequential_percents = []
        self.dict = {}

    def add(self, item):
        '''
        Adds item to triptor

        Item must be hashable! 
        '''
        if item in self.dict:
            ndx = self.dict[item]       
            self.count_of_items[ndx] += 1
        else:
            self.list_of_items.append(item)
            self.count_of_items.append(1)
            self.dict[item] = len(self.list_of_items) - 1

    def build_percents(self):
        '''
        Builds both normal percentages, and sequential selection percentages.
        '''
        length = len(self.list_of_items)
        total_items = sum(self.count_of_items)

        self.normal_chance = [0.0] * length
        self.sequential_percents = [0.0] * length

        # First, go through and calculate aaaalll the item ratios
        for item_index in range(length):
            item_chance = self.count_of_items[item_index] / total_items
            self.normal_chance[item_index] = item_chance

        # Next, rig 'em up to go one-by-one :)
        previous_product = 1
        for item_index in range(length):
            sequential_chance = self.normal_chance[item_index] / previous_product
            self.sequential_percents[item_index] = sequential_chance
            if sequential_chance >= 1:
                #print('...nani?')
                break
            previous_product = previous_product * (1 - sequential_chance)

        #print(self.list_of_items)
        self.sequential_percents[length - 1] = 1  # that'll fix those floating point errors!
        
    def choice(self, rebuild_percents = True):
        '''
        Picks a nice happy item from the histogram.   

        Pass it a False to prevent rebuilding of the chances. Nice if you
        don't want to do that a gajillion times.
        '''
        
        if rebuild_percents:
            self.build_percents()

        #print(len(self.sequential_percents))
        #print(len(self.list_of_items))

        for item_index in range(len(self.list_of_items)):
            item_chance = self.sequential_percents[item_index]
            if item_chance > random.random():
                return self.list_of_items[item_index]
   
    def remove(self, item):
        '''
        Lookup is fast, probably

        Returns true if object 'item' was found and removed from the Triptor, 
        returns false if object 'item' was not removed. (not in list, or 0 in hist)

        Note: I have no idea if this works.
        '''
        if item in self.dict:
            ndx = self.dict[item]
            if self.count_of_items[ndx] < 1:
                self.count_of_items[ndx] = 0
                return False
            else:
                self.hist[ndx] -= 1
                return True
        else:
            return False


def test_normal():
    histogram = NormalHistogram('Stanley')
    histogram.add('one')
    histogram.add('fish')
    histogram.add('two')
    histogram.add('fish')
    histogram.add('red')
    histogram.add('fish')
    histogram.add('blue')
    histogram.add('fish')
    histogram.build_percents()

    print(histogram.list_of_items)
    print(histogram.count_of_items)
    print(histogram.normal_chance)
    print(histogram.sequential_percents)


def test_triptor():
    triptor = Triptor('The')
    triptor.add(1)
    triptor.add(3)
    triptor.add(7)
    triptor.add(1)

    assert triptor.hist[0] == 2


if __name__ == "__main__":
    test_normal()