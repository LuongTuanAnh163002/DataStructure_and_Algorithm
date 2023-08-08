class node:
    def __init__(self, data):
        self._data = data
        self._next = None
        
class queues:
    def __init__(self):
        self._head = None
        self._last = None
        self._size = 0
    def isempty(self):
        return self._size == 0
    
    def length(self):
        return self._size
    
    def enqueue(self, key):
        new_node = node(key)
        if self.isempty():
            self._head = self._last = new_node
            self._size += 1
        else:
            self._last._next = new_node
            self._last = new_node
            self._size += 1
            
    def dequeue(self):
        if self.isempty():
            return None
        else:
            tmp = self._head
            self._head = tmp._next
            self._size -= 1
            return tmp._data
    def first(self):
        if self.isempty():
            print("queue is empty")
        else:
            return self._head._data
        
    def lasts(self):
        if self.isempty():
            print("queue is empty")
        else:
            return self._last._data
        
    def display(self):
        tmp = self._head
        while tmp:
            print(tmp._data, end = " ")
            tmp = tmp._next
                    
a = queues()
a.enqueue(1)
a.enqueue(2)
a.enqueue(3)
a.display()