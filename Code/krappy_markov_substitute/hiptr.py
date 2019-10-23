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


def test_triptor():
    triptor = Triptor('The')
    triptor.add(1)
    triptor.add(3)
    triptor.add(7)
    triptor.add(1)

    assert triptor.hist[0] == 2
