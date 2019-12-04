


class Node(object):
    def __init__(self, data = None, next_node = None):
        self.next = next_node
        self.data = data

class LonkedList(object):
    def __init__(self, init_list = [], start_length = 0, default_data = None):
        self.count = 0
        self.head = None
        self.tail = None

        for i in init_list:
            self.append(i)

    def is_empty(self):
        '''
        Always O(1), just returning a bool, here
        '''
        return bool(self.head)

    def items(self, process=lambda data: data):
        '''
        Always O(n), c'mon, what'd you expect? 

        pass a lambda process for fun & profit
        '''
        retlist = []
        node = self.head
        while node is not None:
            retlist.append(process(node.data))
            node = node.next
        return retlist
    
    def append(self, data):
        '''
        Always O(1), it's just plopped in back
        '''
        new_node = Node(data)
        self.count += 1
        if self.tail != None:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def prepend(self, data):
        '''
        Always O(1), it's just plopped in front
        '''
        new_node = Node(data, self.head)
        self.count += 1
        if self.tail != None:
            self.head = new_node 
        else:
            self.head = new_node
            self.tail = new_node
    
    def length(self):
        '''
        Always O(1), we're literally just returning a number here
        '''
        return self.count

    def absolute_length(self):
        '''
        Always O(n), linear counter. Definitely correct. 
        '''
        node = self.head
        count = 0
        while node != None:
            node = node.next
            count += 1
        self.count = count
    
    def find(self, quality):
        '''
        '''
        node = self.head
        while node != None:
            if quality(node.data):
                return node.data
            node = node.next
        #return False

    def old_find(self, item):
        '''
        O(n) average/worst case, O(1) best case if the item is contained
        in the first node.
        '''
        node = self.head
        while node != None:
            if node.data == item:
                return node.data
            node = node.next
        #raise ValueError

    def delete(self, item=None, quality=None):
        '''
        O(n) average/worst case, O(1) best case if the item is contained
        in the first node.
        '''
        p_node = None
        node = self.head
        while node != None:
            if quality is not None:
                if quality(node.data):
                    if node == self.tail:
                        self.tail = p_node
                    if node != self.head:
                        p_node.next = node.next
                        self.count -= 1
                        return #d4ful
                    else:
                        self.head = node.next
                        self.count -= 1
                        return #d4ful

            elif node.data == item:
                if node == self.tail:
                    self.tail = p_node
                if node != self.head:
                    p_node.next = node.next
                    self.count -= 1
                    return #d4ful
                else:
                    self.head = node.next
                    self.count -= 1
                    return #d4ful
            p_node = node
            node = node.next
        raise ValueError


