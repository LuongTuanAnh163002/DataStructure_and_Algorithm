class vertex:
    def __init__(self, data):
        self.data = data
        self.neiborhood = []
        
    def add_neibor(self, value):
        if value not in self.neiborhood:
            self.neiborhood.append(value)
            self.neiborhood.sort()
            
class Graph:
    def __init__(self):
        self.vertice = {}
    
    def add_vertice(self, ver):
        if ver.data not in self.vertice:
            self.vertice[ver.data] = ver
        else:
            print("Vertex is exist")
            
    def add_edge(self, u, v):
        if u in self.vertice and v in self.vertice:
            for key, value in self.vertice.items():
                if key == u:
                    value.add_neibor(v)
                if key == v:
                    value.add_neibor(u)
                    
        else:
            print(str(u) + " or " + str(v) + " is not a vertex of Graph")
        
    def number_vertex(self):
        return len(self.vertice)
    
    def print_graph(self):
        for key in sorted(list(self.vertice.keys())):
            print(str(key) + ":" + str(self.vertice[key].neiborhood))
            
grph = Graph()
grph.add_vertice(vertex(1))
grph.add_vertice(vertex(0))
grph.add_vertice(vertex(2))
grph.add_vertice(vertex(3))
grph.add_vertice(vertex(4))
grph.add_edge(0, 4)
grph.add_edge(4, 0)
grph.add_edge(0, 1)
grph.add_edge(1, 0)
grph.add_edge(1, 2)
grph.add_edge(2, 1)
grph.add_edge(1, 3)
grph.add_edge(3, 1)
grph.add_edge(1, 4)
grph.add_edge(4, 1)
grph.add_edge(3, 4)
grph.add_edge(4, 3)
grph.add_edge(2, 3)
grph.add_edge(3, 2)
grph.print_graph()
print(grph.number_vertex())


                
    
        