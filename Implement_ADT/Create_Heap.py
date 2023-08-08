class Heap:
    def __init__(self, category = "maxheap"):
        self.data = []
        self.category = category
        
    def parent(self, j):
        return (j - 1) // 2
    
    def left(self, j):
        return 2 * j + 1
    
    def right(self, j):
        return 2 * j + 2
    
    def swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]
        
    def upheapmax(self, j):
        par = self.parent(j)
        if j > 0 and self.data[par] < self.data[j]:
            self.swap(par, j)
            self.upheapmax(par)
            
    def upheapmin(self, j):
        par = self.parent(j)
        if j > 0 and self.data[par] > self.data[j]:
            self.swap(par, j)
            self.upheapmin(par)
            
    def add(self, value):
        self.data.append(value)
        if category = "maxheap":
            self.upheapmax(len(self.data) - 1)
        else:
            self.upheapmin(len(self.data) - 1)
            
    def _len_(self):
        return len(self.data)
    
    def min_element(self):
        pass
        #.............
            
    def downheap(self, j):
        pass
        #..............
    
    def delete(self):
        pass
        #.............
    

    
    
    
    