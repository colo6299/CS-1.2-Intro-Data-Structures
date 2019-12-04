from lonkedlist import LonkedList as LinkedList


class CrashTable(object):

    def __init__(self, start_size = 8):
        self.item_count = 0
        self.buckets = []
        for i in range(start_size):
            self.buckets.append(LinkedList())

    def bindexer(self, key):
        return hash(key) % len(self.buckets)

    def data_by_key(self, key, bindex=None):
        if bindex is None:
            bindex = self.bindexer(key) 
        return self.buckets[bindex].find(lambda node_data: node_data[0] == key)

    def list_by_key(self, key, bindex=None):
        if bindex is None:
            bindex = self.bindexer(key)
        return self.buckets[bindex]

    def absolute_length(self):
        count = 0
        for ll in self.buckets:
            count += ll.absolute_length()
        return count

    def length(self):
        return self.item_count

    def contents_by_lambda(self, process=None):
        # Shameless rip from starter code lol
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items(process))
        return all_items

    def items(self):
        return self.contents_by_lambda(lambda data: data)
        
    def keys(self):
        return self.contents_by_lambda(lambda data: data[0])

    def values(self):
        return self.contents_by_lambda(lambda data: data[1])

    def set(self, key, value):
        bindex = self.bindexer(key)
        data = self.data_by_key(key, bindex)
        if data:
            data[1] = value
        else:
            self.buckets[bindex].append([key, value])
            self.item_count += 1

    def get(self, key):
        data = self.data_by_key(key)
        if data:
            return data[1]
        else:
            raise KeyError

    def delete(self, key, suppress=False):
        try:
            self.list_by_key(key).delete(quality=lambda data: data[0] == key)
            self.item_count -= 1
        except ValueError:
            raise KeyError
        

    def contains(self, key):
        
        if self.list_by_key(key).find(quality=lambda data: data[0] == key):
            return True
        else: 
            return False
