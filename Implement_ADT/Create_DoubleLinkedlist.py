'''
class node:
    def __init__(self, data):
        self.prev = None
        self.next = None
        self.data = data
        
class doublelink:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def is_empty(self):
        return self.size == 0
        
    def addtohead(self, key):
        new_node = node(key)
        if self.head is None:
            self.head = new_node
            self.size += 1
            
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.size += 1
            
    def addtoafter(self, prev, key):
        new_node = node(key)
        if prev is None:
            print("Error")
        else:
            new_node.next = prev.next
            new_node.prev = prev
            prev.next = new_node
            new_node.next.prev = new_node
            self.size += 1
            
    def addtotail(self, key):
        new_node = node(key)
        if self.head is None:
            self.head = new_node
            self.size += 1
        else:
            tmp = self.head
            while tmp.next:
                tmp = tmp.next
            tmp.next = new_node
            new_node.prev = tmp
            self.size += 1
        
    def traverse(self):
        tmp = self.head
        while tmp:
            print(tmp.data, end = " ")
            last = tmp
            tmp = tmp.next
        print("\n")
        while last:
            print(last.data, end = " ")
            last = last.prev
        
    def _len_(self):
        return self.size
    
    def top(self):
        return self.head.data
        
double1 = doublelink()
double1.insertfront(1)
double1.insertfront(2)
double1.insertfront(3)
'''
#c2
class node:
    def __init__(self, data):
        self.prev = None
        self.next = None
        self.data = data
    
class doublelink:
    def __init__(self):
        self.header = node(None)
        self.trailer = node(None)
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0
        self.total = 0
    
    def isempty(self):
        return self.size == 0
    
    def _len_(self): #function 1
        return self.size
    
    def insert_between(self, key, pre, aft): #function 2
        new_node = node(key)
        pre.next = new_node
        aft.prev = new_node
        new_node.next = aft
        new_node.prev = pre
        self.size += 1
        self.total += key
        
    def delete_node(self, node): #function 3
        pre = node.prev
        aft = node.next
        pre.next = aft
        aft.prev = pre
        self.size -= 1
        element = node.data
        self.total -= element
        return element
    
    def addtohead(self, key): #function 4
        self.insert_between(key, self.header, self.header.next)
        
    def addtotail(self, key): #function 5
        self.insert_between(key, self.trailer.prev, self.trailer)
        
        
    def deletefromhead(self): #function 6
        a = self.delete_node(self.header.next)
        return a
    
    def deletefromtail(self): #function 7
        a = self.delete_node(self.trailer.prev)
        return a
    
    def _sum_(self): #function 8
        return self.total
    
    def average(self): #function 9
        return self.total / self.size
    
    def toarray(self): #funtion 10
        tmp = self.header.next
        lst = []
        while tmp.data:
            lst.append(tmp.data)
            tmp = tmp.next
        return lst
    
    def maxs(self): #function 11
        lst = self.toarray()
        lst.sort()
        return lst[-1]
    
    def mins(self): #function 12
        lst = self.toarray()
        lst.sort()
        return lst[0]
    
    def first(self): #function 13
        return self.header.next.data
    
    def last(self): #funtion 14
        return self.trailer.prev.data
    
    def traverse(self): #funtion 15
        tmp = self.header.next
        while tmp.data:
            print(tmp.data, end = " ")
            tmp = tmp.next
            
double1 = doublelink()
double1.addtohead(1)
double1.addtohead(2)
double1.addtohead(3)
double1.addtohead(4)
double1.addtotail(5)
double1.addtotail(6)
double1.deletefromhead()
double1.deletefromtail()
print("The len of doublelink:", double1._len_())
print("The sum of doublelink:", double1._sum_())
print("The average:", double1.average())
print("Max:", double1.maxs())
print("Min:", double1.mins())
print("Array:", double1.toarray())
print("The first element:", double1.first())
print("The last element:", double1.last())
double1.traverse()

