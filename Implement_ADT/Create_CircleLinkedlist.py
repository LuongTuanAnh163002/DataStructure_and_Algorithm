class node:
    def __init__(self, data):
        self._data = data
        self._next = None
        
class circlelink:
    def __init__(self):
        self._tail = None
        self._size = 0
        self._total = 0
        
    def is_empty(self):
        return self._size == 0
    
    def _len_(self): #function 1
        return self._size
    
    def _sum_(self): #funtion 2
        return self._total
    
    def average(self): #function 3
        return self._total / self._size
    
    def addtohead(self, key): #funtion 4
        new_node = node(key)
        if self._tail is None:
            new_node._next = new_node
            self._tail = new_node
            self._size += 1
            self._total += new_node._data
        else:
            new_node._next = self._tail._next
            self._tail._next = new_node
            self._size += 1
            self._total += new_node._data
            
    def addtotail(self, key): #funtion 5
        new_node = node(key)
        if self._tail is None:
            new_node._next = new_node
            self._tail = new_node
            self._size += 1
            self._total += new_node._data
        else:
            new_node._next = self._tail._next
            self._tail._next = new_node
            self._tail = new_node
            self._size += 1
            self._total += new_node._data
            
    def addafter(self, prev, key): #function 6
        new_node = node(key)
        if prev is None:
            print("Error")
        
        elif prev == self._tail:
            self.addtotail(key)
            self._size += 1
            self._total += new_node._data
        else:
            new_node._next = prev._next
            prev._next = new_node
            self._size += 1
            self._total += new_node._data
            
    def traverse(self): #function 7
        tmp = self._tail._next
        if self._tail._next is not None:
            
            while tmp._next != self._tail._next:
                print(tmp._data, end = " ")
                tmp = tmp._next
            print(tmp._data)
            
    def toarray(self): #function 8
        lst = []
        tmp = self._tail._next
        while tmp._next != self._tail._next:
            lst.append(tmp._data)
            tmp = tmp._next
        lst.append(tmp._data)
        return lst
        
    def maxs(self): #function 9
        lst = self.toarray()
        lst.sort()
        return lst[-1]
    
    def mins(self): #function 10
        lst = self.toarray()
        lst.sort()
        return lst[0]
    
    def deletefromhead(self): #function 11
        if self._tail is None:
            return None
        else:
            a = self._tail._next._data
            self._tail._next = self._tail._next._next
            self._size -= 1
            self._total -= a
            return a
    
    def deletefromtail(self): #function 12
        if self._tail is None:
            return None
        else:
            tmp = self._tail
            while tmp:
                if tmp._next == self._tail:
                    a = self._tail._data
                    tmp._next = self._tail._next
                    self._tail = tmp
                    self._size -= 1
                    self._total -= a
                    return a
                tmp = tmp._next
            
        
a = circlelink()
a.addtohead(1)
a.addtohead(2)
a.addtohead(3)
a.addtohead(4)
a.addtotail(5)
a.addafter(a._tail._next._next, 6)
a.deletefromhead()
a.deletefromtail()

a.traverse()
print("Sum:", a._sum_())
print("Len:", a._len_())
print("Average:", a.average())
print("Array:", a.toarray())
print("Max:", a.maxs())
print("Min:", a.mins())
