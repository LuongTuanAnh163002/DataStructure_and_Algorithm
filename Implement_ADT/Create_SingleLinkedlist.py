class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class linkedlist:
    def __init__(self):
        self.head = None
        self.size = 0
        self.total = 0
    
    def isempty(self):
        return self.size == 0
        
    def addtohead(self, key): #function 1(add a node with value x  at the head of  a list)
        new_node = node(key)
        if self.head is None:
            self.head = new_node
            self.size += 1
            self.total += new_node.data
            
        else:
            new_node.next = self.head
            self.head = new_node
            self.size += 1
            self.total += new_node.data
            
    def addtotail(self, key): #function 2(add a node with value x  at the tail of  a list)
        new_node = node(key)
        if self.head is None:
            self.head = new_node
            self.size += 1
            self.total += new_node.data
            
        else:
            tmp = self.head
            while tmp.next:
                tmp = tmp.next
            tmp.next = new_node
            self.size += 1
            self.total += new_node.data
            
    def addafter(self, prev, key): #function 3(add a node with value x  after the node p)
        new_node = node(key)
        if prev is None:
            print("error")
            
        else:
            new_node.next = prev.next
            prev.next = new_node
            self.size += 1
            self.total += new_node.data
            
    def addbefore(self, aft, key): #function 4(add a node with value x  before the node p)
        new_node = node(key)
        tmp = self.head
        if tmp == aft:
            self.addtohead(key)
        else:
            while tmp:
                if tmp.next == aft:
                    self.addafter(tmp, key)
                    break
                else:
                    tmp = tmp.next
                    
    def traverse(self): #function 5(traverse from head to tail and dislay info of all nodes in the list)
        tmp = self.head
        while tmp:
            print(tmp.data, end = " ")
            tmp = tmp.next
    
    def count(self): #function 6(count and return number of nodes in the list)
        return self.size
    
    def deletefromhead(self): #function 7(delete the head and return its info)
        tmp = self.head
        if tmp is None:
            return None
        else:
            self.head = tmp.next
            self.total -= tmp.data
            self.size -= 1
            return tmp.data
        
    def deletefromtail(self): #function 8(delete the tail and return its info)
        tmp = self.head
        while tmp.next and tmp.next.next:
            tmp = tmp.next
        self.size -= 1    
        self.total -= tmp.next.data
        a = tmp.next.data
        tmp.next = None
        return a
        
    def deleteafter(self, prev): #function 9(delete the node after the node  p  and return its info)
        a = prev.next.data
        self.total -= prev.next.data
        prev.next = prev.next.next
        self.size -= 1
        return a
    
    def del_(self, x): #function 10(delele the first node whose info is equal to x)
        tmp = self.head
        count = 0
        count1 = self.size
        if tmp.data == x:
            self.deletefromhead()
        else:
            while tmp.next:
                if tmp.next.data == x:
                    self.deleteafter(tmp)
                    break
                tmp = tmp.next
                count += 1
            if count == count1 - 1:
                print("Do not exist", x)
            
    def _del(self, i): #function 11(delete an i-th node on the list. Besure that such a node exists)
        tmp = self.head
        cnt = 0
        if i >= self.size:
            print("Error")
            return
        elif i == 0:
            self.deletefromhead()
            return
        else:
            while tmp:
                if cnt == i - 1:
                    self.deleteafter(tmp)
                    break
                else:
                    tmp = tmp.next
                    cnt += 1
        
    def search(self, x): #function 12(search and return the reference to the first node having info x)
        tmp = self.head
        dem = 0
        while tmp:
            if tmp.data == x:
                return True
                break
            tmp = tmp.next
            dem += 1
        if dem == self.size:
            return False
        
    def maxs(self): #function 13(find and return the maximum value in the list)
        arr = self.toarray()
        arr.sort()
        return arr[-1]
    
    def mins(self): #function 14(find and return the minimum value in the list)
        arr = self.toarray()
        arr.sort()
        return arr[0]
        
    def toarray(self): #function 15(create and return array containing info of all nodes in the list)
        tmp = self.head
        arr = []
        while tmp:
            arr.append(tmp.data)
            tmp = tmp.next
        return arr
    
    def sums(self): #function 16(return the sum of all values in the list)
        return self.total
    
    def avg(self): #function 17(return the average of all values in the list)
        return self.total / self.size
    
    def _sorted_(self): #funtion 18(check and return true if the list is sorted, return false if the list is not sorted)
        arr = self.toarray()
        arr1 = arr.copy()
        arr1.sort()
        arr2 = arr.copy()
        arr2.sort(reverse = True)
        if arr == arr1 or arr == arr2:
                  return True
        else:
                  return False
                  
    def _sort_(self): #function 19(sort the list by ascending order of info)
        arr = self.toarray()
        arr.sort(reverse = True)
        a = self.size
        for i in range(0, a):
            b = self.deletefromhead()
            self.size -= 1
        for i in arr:
            self.addtohead(i)
            self.size += 1
        
    def _reverse_(self): #function 20(Reverse a singly linked list using only one pass through the list)
        arr = self.toarray()
        a = self.size
        for i in range(0, a):
            b = self.deletefromhead()
            self.size -= 1
        for i in arr:
            self.addtohead(i)
            self.size += 1
            
    def attach(self, other):
        tmp = self.head
        tmp1 = other.head
        while tmp.next:
            tmp = tmp.next
        tmp.next = other.head
        
        while tmp1:
            self.size += 1
            self.total += tmp1.data
            tmp1 = tmp1.next
        
        
    def checkthesame(self, other):
        if self.size != other.size:
            return False
        else:
            tmp = self.head
            tmp1 = other.head
            count = 0
            while tmp and tmp1:
                if tmp.data != tmp1.data:
                    return False
                else:
                    count += 1
                    tmp = tmp.next
                    tmp1 = tmp1.next
            if count == self.size:
                return True
            else:
                return False
            
    def merge(self, other):
        self.attach(other)
        self._sort_()
        
    def ispalindrome(self):
        arr = self.toarray()
        arr1 = arr.copy()
        arr1.reverse()
        if arr == arr1:
            return True
        else:
            return False
        
    def removeduplicate(self):
        tmp1 = self.head
        tmp2 = None
        while tmp1 != None and tmp1.next != None:
            tmp2 = tmp1
            while tmp2.next != None:
                if tmp1.data == tmp2.next.data:
                    tmp2.next = tmp2.next.next
                    self.size -= 1
                else:
                    tmp2 = tmp2.next
            tmp1 = tmp1.next
            
    def segregate_even_odd(self):
        tmp = self.head
        count = 0
        while tmp.data % 2 != 0:
            self.addtotail(tmp.data)
            self.head = tmp.next
            tmp = tmp.next
            count += 1
            self.size -= 1
        
        while tmp.next != None and count != self.size - 1:
            if tmp.next.data % 2 != 0:
                self.addtotail(tmp.next.data)
                tmp.next = tmp.next.next
                count += 1
                self.size -= 1
            else:
                tmp = tmp.next
                count += 1
                
        
        
            
ll1 = linkedlist()
ll2 = linkedlist()

ll2.addtohead(3)
ll2.addtohead(4)
ll2.addtohead(9)
ll2.addtohead(8)

ll1.addtohead(4)
ll1.addtohead(3)
ll1.addtohead(7)
ll1.addtohead(1)

ll1.addtotail(5)
ll1.addtotail(6)
ll1.addtotail(8)

ll1.addafter(ll1.head.next, 9)

ll1.addbefore(ll1.head.next, 10)

ll1.deletefromhead()
ll1.deletefromtail()
ll1.deleteafter(ll1.head.next)
ll1.del_(10)
ll1._del(3)

print("Element in Linklist:", ll1.search(11))
print("Max:", ll1.maxs())
print("Min:", ll1.mins())
print("Sum:", ll1.sums())
print("Average:", ll1.avg())
print("Len:", ll1.count())
print("Array:", ll1.toarray())
ll1._sort_()
print("Linkedlist is sorted:", ll1._sorted_())
ll1._reverse_()
ll1.traverse()
#ll1.attach(ll2)
print()
ll1.traverse()
print()
print("Length after attach:", ll1.size)
print("Total after attach:", ll1.total)
print("Two linklist is the same:", ll1.checkthesame(ll2))
ll1.merge(ll2)
ll1.traverse()



            
