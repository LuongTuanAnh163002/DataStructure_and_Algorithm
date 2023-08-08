class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class stacks:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def isempty(self):
        return self.size == 0
        
    def push(self, data):
        new_node = node(data)
        if self.head == None:
            self.head = new_node
            
        else:
            new_node.next = self.head
            self.head = new_node
            self.size += 1
            
    def pop(self):
        if self.isempty():
            return None
        else:
            rev_node = self.head
            self.head = self.head.next
            rev_node.next = None
            self.size -= 1
            return rev_node.data
        
    def length(self):
        return self.size
    
    def top(self):
        if self.isempty():
            return None
        else:
            return self.head.data
        
    def traverse(self):
        if self.isempty():
            print("stack overflow")
        else:
            tmp = self.head
            while tmp:
                print(tmp.data, end = " ")
                tmp = tmp.next
                
a = stacks()
a.push(1)
a.push(2)
a.push(3)
a.traverse()
    
    
        
    