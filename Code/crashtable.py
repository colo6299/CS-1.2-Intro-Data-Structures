from lonkedlist import LonkedList as LinkedList


class CrashTable(object):

    def __init__(self, start_size = 8, mode='Static'):
        self.item_count = 0
        self.mode = mode
        self.buckets = []
        for i in range(start_size):
            self.buckets.append(LinkedList())

    def __str__(self):  # Yoink
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):  # Yoooink
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def bindexer(self, key):
        '''
        Believe it or not, I didn't copy-paste this
        '''
        return hash(key) % len(self.buckets)

    def data_by_key(self, key, bindex=None):
        '''
        had to move to SF because the rent in the database was too high
        '''
        if bindex is None:
            bindex = self.bindexer(key) 
        return self.buckets[bindex].find(lambda node_data: node_data[0] == key)

    def list_by_key(self, key, bindex=None):
        '''
        gets a list, probably
        '''
        if bindex is None:
            bindex = self.bindexer(key)
        return self.buckets[bindex]

    def absolute_length(self):
        '''
        Are you a paranoid schizophenic? This is for you!

        O(n + b) all cases
        '''
        count = 0
        for ll in self.buckets:
            count += ll.absolute_length()
        return count

    def length(self):
        '''
        take a wild guess

        O(1) all cases
        '''
        return self.item_count

    def contents_by_lambda(self, process=None):
        '''
        Not for you, bucko
        '''
        # Shameless rip from starter code lol
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items(process))
        return all_items

    def items(self):
        '''
        Returns a list of all key-value pairs in hashtable

        O(n + b) for all cases
        '''
        return self.contents_by_lambda(lambda data: data)
        
    def keys(self):
        '''
        Returns a list of all keys in hashtable

        O(n + b) for all cases
        '''
        return self.contents_by_lambda(lambda data: data[0])

    def values(self):
        '''
        Returns a list of all values in hashtable

        O(n + b) for all cases
        '''
        return self.contents_by_lambda(lambda data: data[1])

    def set(self, key, value):
        '''
        Updates or creates new key value pair

        O(l) average case runtime
        '''
        bindex = self.bindexer(key)
        data = self.data_by_key(key, bindex)
        if data:
            data[1] = value
        else:
            self.buckets[bindex].append([key, value])
            self.item_count += 1

    def get(self, key):
        '''
        Returns value associated with key

        O(l) average case runtime
        '''
        data = self.data_by_key(key)
        if data:
            return data[1]
        else:
            raise KeyError

    def delete(self, key, suppress=False):
        '''
        Delete selected key from hashtable

        O(l) average case runtime 
        '''
        try:
            self.list_by_key(key).delete(quality=lambda data: data[0] == key)
            self.item_count -= 1
        except ValueError:
            raise KeyError
        

    def contains(self, key):
        '''
        Returns true if the key is found in the hashtable

        O(l) average case runtime
        '''
        if self.list_by_key(key).find(quality=lambda data: data[0] == key):
            return True
        else: 
            return False
