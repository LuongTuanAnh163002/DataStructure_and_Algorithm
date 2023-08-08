from collections import deque
from queue import PriorityQueue
class Graph:
    def __init__(self, V, E, is_directed = False, is_weighted = True):
        self.Vertices = V
        self.Edges = E
        self.is_directed = is_directed
        self.is_weighted = is_weighted
        self.adjancencylist = self.adjacency_list2(V, E) if is_weighted else self.adjacency_list1(V, E)
        self.adjancencymat = self.adjacency_mat2(V, E) if is_weighted else self.adjacency_mat1(V, E)
        
    def adjacency_list1(self, vertex_lst, edge_lst): #Function 1 ok
        adj_list = {v:[] for v in vertex_lst}
        for e in edge_lst:
            node1, node2 = e[0], e[1]
            adj_list[node1].append(node2)
            if not self.is_directed:
                adj_list[node2].append(node1)
                
        return adj_list
    
    def adjacency_list2(self, vertex_lst, edge_lst):#Function 2 ok
        adj_list = {v: {} for v in vertex_lst}
        for e in edge_lst:
            node1, node2 = e[0], e[1]
            lst = []
            for i in range(2, len(e)):
                lst.append((node2, e[i]))
            adj_list[node1][node2] = lst
            if not self.is_directed:
                lst1 = []
                for i in range(2, len(e)):
                    lst1.append((node1, e[i]))
                adj_list[node2][node1] = lst1
        return adj_list
    
    def adjacency_mat1(self, vertex_lst, edge_lst): #Function 3 ok
        adj_mat = [[0 for v in vertex_lst] for c in vertex_lst]
        for e in edge_lst:
            node1, node2 = e[0], e[1]
            indx1 = self.Vertices.index(node1)
            indx2 = self.Vertices.index(node2)
            adj_mat[indx1][indx2] = 1
            if not self.is_directed:
                adj_mat[indx2][indx1] = 1
        
        return adj_mat
    
    def adjacency_mat2(self, vertex_lst, edge_lst): #Function 4 ok
        adj_mat = [[0 for i in vertex_lst] for c in vertex_lst]
        for e in edge_lst:
            node1, node2, node3 = e[0], e[1], min(e[2:len(e)])
            indx1 = vertex_lst.index(node1)
            indx2 = vertex_lst.index(node2)
            adj_mat[indx1][indx2] = node3
            if not self.is_directed:
                adj_mat[indx2][indx1] = node3
        return adj_mat
    
    def DFS(self, start, visited = set()): #Function 5 ok
        if start not in visited:
            visited.add(start)
            print(start, end = " ")
        for i in self.adjancencylist[start]:
            if i not in visited:
                self.DFS(i, visited)
    
    def BFS(self, start, visited = set()): #Function 6 ok
        if start not in self.Vertices:
            return
        Q = deque()
        Q.append(start)
        while len(Q) != 0:
            v = Q.popleft()
            if v not in visited:
                visited.add(p)
                print(p, end = " ")
                for w in self.adjancencylist[v]:
                    if w not in visited:
                        Q.append(w)
                        
    def insert_vertex(self, vertex): #Funtion 7 ok 
        self.Vertices.append(vertex)
        
    def insert_edge(self, vertex_source, vertex_goal): #Function 8 ok
        if self.is_weighted == True:
            print("You can not access this function in this case")
            return
        else:
            if vertex_goal not in self.Vertices:
                return
            lst = [vertex_source, vertex_goal]
            self.Edges.append(lst)
            self.adjancencylist = self.adjacency_list1(self.Vertices, self.Edges)
            self.adjancencymat = self.adjacency_mat1(self.Vertices, self.Edges)
        
    def insert_weighted_edge(self, vertex_source, vertex_goal, arr): #function 9 ok
        if self.is_weighted == False:
            print("You can not access this function in this case")
            return
        else:
            if vertex_goal not in self.Vertices:
                return
            lst = [vertex_source, vertex_goal] + arr
            self.Edges.append(lst)
            self.adjancencylist = self.adjacency_list2(self.Vertices, self.Edges)
            self.adjancencymat = self.adjacency_mat2(self.Vertices, self.Edges)
        
        
    def number_vertex(self): #Function 10 ok
        return len(self.Vertices)
    
    def number_edge(self): #Function 11 ok
        if self.is_weighted == True:
            length = 0
            for i in self.Edges:
                length += len(i[2:])
            return length
        else:
            return len(self.Edges)
    
    def delete_vertex(self, vertex): #Function 12 ok
        if vertex not in self.Vertices:
            print("Value is not exist")
            return
        self.Vertices.remove(vertex)
        
    def delete_edge(self, vertex): #Function 13 ok
        lst = []
        for e in self.Edges:
            if vertex not in e:
                lst.append(e)
        self.Edges = lst
        if self.is_weighted == False:
            self.adjancencylist = self.adjacency_list1(self.Vertices, self.Edges)
            self.adjancencymat = self.adjacency_mat1(self.Vertices, self.Edges)
        else:
            self.adjancencylist = self.adjacency_list2(self.Vertices, self.Edges)
            self.adjancencymat = self.adjacency_mat2(self.Vertices, self.Edges)
        
    def vertex_neiborhood(self, vertex): #function 14 ok
        if self.is_weighted == False:
            return self.adjancencylist[vertex]
        else:
            return list(self.adjancencylist[vertex].keys())
    
    def dijkstra1(self, start_vertex):#Function 15 | Cách 1: Sử dụng PriorityQueue trong module queue trong python và adjacencymatrix
        if self.isweighted:
            D = {v: [float('inf'), 0] for v in self.Vertices}
            pq = PriorityQueue()
            D[start_vertex][0] = 0
            D[start_vertex][1] = start_vertex
            pq.put((0, start_vertex))
            visit_lst = []
            matrix = self.AdjacencyMat
            while not pq.empty():
                (dist, current_vertex) = pq.get()
                visit_lst.append(current_vertex)
            
                for neighbor in self.Vertices:
                    indx1 = self.Vertices.index(current_vertex)
                    indx2 = self.Vertices.index(neighbor)
                    if matrix[indx1][indx2] != 0:
                        distance = matrix[indx1][indx2]
                        if neighbor not in visit_lst:
                            old_dist = D[neighbor][0]
                            new_dist = D[current_vertex][0] + distance
                            if new_dist < old_dist:
                                pq.put((new_dist, neighbor))
                                D[neighbor][0] = new_dist
                                D[neighbor][1] = current_vertex
            return D
        else:
            return "Can not excute dijkstra algorithm because Graph is not weighted"
        
    def prim_jarnick(self, start_vertex):#minimum spanning tree algorithm
        pq = PriorityQueue()
        pq.put((0, start_vertex, start_vertex))
        visit_lst = []
        display_lst = []
        matrix = self.adjancencymat
        while not pq.empty():
                (dist, current_vertex, parent_vertex) = pq.get()
                if current_vertex not in visit_lst:
                    visit_lst.append(current_vertex)
                    display_lst.append([parent_vertex, current_vertex, dist])
                for neibor in self.Vertices:
                    a = self.Vertices.index(current_vertex)
                    b = self.Vertices.index(neibor)
                    if matrix[a][b] != 0:
                        distance = matrix[a][b]
                        if neibor not in visit_lst:
                            pq.put((distance, neibor, current_vertex))
        return display_lst[1:]

V = ['A','B','C','D','E','F', 'G', 'H', 'I']
E = [['A','B', 4], ['A','C', 7], ['B','C', 11], ['B','D', 9], ['B','F', 20], ['C','F', 1], ['D','E', 2], ['E','F', 1], ['D','G',6],
     ['E', 'G', 10], ['E', 'H', 5], ['E', 'I', 15], ['F', 'H', 3], ['G', 'I', 5], ['H', 'I', 12]]
G = Graph(V, E, is_weighted = True)
dic = G.adjancencylist
for c in dic.keys():
    print(c, dic[c])

for i in G.prim_jarnick("A"):
    print(i[0] + ' - ' + i[1] + ': ' + str(i[2]))

    
    
    
    
    
        
    
        
            
        
                
        