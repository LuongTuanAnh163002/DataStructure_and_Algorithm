class node:
    def __init__(self, element):
        self.element = element
        self.parent = None
        self.children = []
        
class Tree:
    def __init__(self):
        self.root = None
        self.size = 0
        self.total = 0
        
    def is_empty(self): #Function 1: Kiểm tra Tree có trống không
        return self.size == 0
        
    def _len_(self): #Function 2: Trả về số lượng phần tử của Tree
        return self.size
    
    def _sum_(self): #Function 3: Trả về tổng các phần tử trong Tree
        return self.total
    
    def average(self): #Function 4: Trả về trung bình cộng
        if self.size == 0 and self.total == 0:
            print("Can not excute this function")
        else:
            return self.size / self.total
    
    def is_root(self, key): #Function 5: Kiểm tra xem giá trị đấy có phải root ko
        if self.is_empty():
            print("Tree is empty")
        else:
            if key == self.root.element:
                return True
            else:
                return False
    
    def add_root(self, key): #Function 6: Thêm root
        if self.root is not None:
            print("Root is exist")
            
        else:
            new_node = node(key)
            self.root = new_node
            self.size += 1
            
            
    def get_node(self, node, ele):#Function 7: Trả về một Tree Object
        if node.element == ele:
            return node
         
        for i in node.children:
            a = self.get_node(i, ele)
            if a == None:
                continue
            else:
                return a
    
    def _parent_(self, val):#Function 8: Trả về giá trị của node cha của node cần tìm
        a = self.get_node(self.root, val)
        b = a.parent.element
        return b
    
    def num_children(self, val):#Function 9: Trả về số node con của 1 node bất kỳ
        a = self.get_node(self.root, val)
        count = 0
        for i in a.children:
            count += 1
        return count
    
    def is_leaf(self, val):#Function 10: Kiểm tra xem node đấy có phải external node ko
        a = self.get_node(self.root, val)
        if len(a.children) == 0:
            return True
        else:
            return False
            
    def add_child(self, ele, key): #Function 11:Thêm vào một node
        new_node = node(key)
        a = self.get_node(self.root, ele)
        new_node.parent = a
        a.children.append(new_node)
        self.size += 1
        
    
    def preorder(self, p): #Function 12:In ra hết tất cả các phần tử trong Tree
        print(p.element)
        for i in p.children:
            self.preorder(i)
            
    def postorder(self, p): #Funtion 13: In ra hết tất cả các phần tử trong Tree
        for i in p.children:
            self.postorder(i)
        print(p.element)
        
    def depth(self, val): #Function 14: Tìm depth của một node bất kì
        a = self.get_node(self.root, val)
        if val == self.root.element:
            return 0
        else:
            return 1 + self.depth(a.parent.element)
            
tree1 = Tree()

tree1.add_root("Book")
tree1.add_child("Book", "Chap1")
tree1.add_child("Book", "Chap2")
tree1.add_child("Book", "Appendix")
tree1.add_child("Chap1", "1.1")
tree1.add_child("Chap1", "1.2")
tree1.add_child("Chap1", "1.3")
tree1.add_child("Chap2", "2.1")
tree1.add_child("Chap2", "2.2")
tree1.add_child("2.2", "2.2.1")
tree1.add_child("2.2", "2.2.2")
# print("Duyệt hết các phần tử trong Tree theo preorder:")
# tree1.preorder(tree1.root)
# print("-------------")
# print("Tree trống:", tree1.is_empty())
# print("Tổng số phần tử trong Tree:", tree1._len_())
# #tree1.postorder(tree1.root)
# print("Kiểm tra Node Chap1 có phải root không:", tree1.is_root("Chap1"))
# print("Giá trị Node cha của Node 2.2.1:", tree1._parent_("2.2.1"))
# print("Số Node con của Node Chap2 là:", tree1.num_children("Chap2"))
# print("Kiểm tra Node 2.2 có phải External không:", tree1.is_leaf("2.2"))
# print("Độ sâu của Node Appendix là:", tree1.depth("Appendix"))
#print(tree1.get_node(tree1.root, "1.1"))


        
    
        
        
        
    
    