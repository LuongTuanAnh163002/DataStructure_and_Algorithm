class Node:
    def __init__(self, element):
        self.left = None
        self.right = None
        self.element = element
        self.parent = None
        
class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0
        self.total = 0
        
    def is_empty(self): #Function 1: Kiểm tra xem BinaryTree có trống không
        return self.size == 0
    
    def _len_(self): #Function 2: Trả về số phần tử trong BinaryTree
        return self.size
    
    def _sum_(self): #Function 3: Tính tổng các phần tử trong BinaryTree
        return self.total
    
    def average(self): #Function 4: Tính trung bình cộng các phần tử trong mảng
        return self.total / self.size
    
    def add_root(self, key): #Function 5: Thêm root vào BinaryTree
        if self.root is not None:
            print("This binary is exist Root")
        else:
            new_node = Node(key)
            self.root = new_node
            self.size += 1
    
    def get_node(self, node, ele): #Function 6: Trả về Node với giá trị cần tìm  kiếm
        if node.element == ele:
            return node
         
        for i in [node.left, node.right]:
            if i:
                a = self.get_node(i, ele)
                if a == None:
                    continue
                else:
                    return a
    
    def num_children(self, ele): #Function 7: Trả về số Node con của giá trị Node cần tìm
        a = self.get_node(self.root, ele)
        count = 0
        if a.right:
            count += 1
        if a.left:
            count += 1
        return count
    
    def add_right(self, ele, key): #Function 8: thêm Node mới vào bên phải
        a = self.get_node(self.root, ele)
        if a.right is not None:
            print("Node " + str(ele) + " is exist Node.right")
        else:
            new_node = Node(key)
            a.right = new_node
            new_node.parent = a
            self.size += 1
            
    def add_left(self, ele, key): #Function 9: thêm Node mới vào bên trái
        a = self.get_node(self.root, ele)
        if a.left is not None:
            print("Node " + str(ele) + " is exist Node.left")
        else:
            new_node = Node(key)
            a.left = new_node
            new_node.parent = a
            self.size += 1
            
    def is_root(self, ele): #Function 10: Kiểm tra giá trị nhập vào có phải root ko
        if self.is_empty():
            print("Binary is empty")
        else:
            if ele == self.root.element:
                return True
            else:
                return False
    
    def left(self, ele): #Function 11: Trả về giá trị của Node trái của Node cần tìm
        a = self.get_node(self.root, ele)
        if a.left:
            return a.left.element
        else:
            return None
    
    def right(self, ele): #Function 12: Trả về giá trị của Node phải của Node cần tìm 
        a = self.get_node(self.root, ele)
        if a.right:
            return a.right.element
        else:
            return None
        
    def _parent_(self, ele): #Function 13: Trả về giá trị Node cha của Node cần tìm
        if ele == self.root.element:
            return None
        else:
            a = self.get_node(self.root, ele)
            return a.parent.element
    
    def is_leaf(self, ele): #Function 14: Kiểm tra Node đấy có phải external Node ko
        if self.num_children(ele) == 0:
            return True
        else:
            return False
        
    def inorder(self, p): #Function 15: Duyệt hết tất cả các phần tử trong BinaryTree
        if p.left:
            self.inorder(p.left)
        print(p.element)
        if p.right:
            self.inorder(p.right)
            
    def preorder(self, p): #Function 16: Duyệt hết tất cả các phần tử trong BinaryTree
        print(p.element)
        if p.left:
            self.preorder(p.left)
        if p.right:
            self.preorder(p.right)
            
    def postorder(self, p): #Function 17: Duyệt hết tất cả các phần tử trong BinaryTree
        if p.left:
            self.postorder(p.left)
        if p.right:
            self.postorder(p.right)
        print(p.element)
        
    
bin1 = BinaryTree()
bin1.add_root("Book")
bin1.add_right("Book", "Chap2")
bin1.add_left("Book", "Chap1")
bin1.add_left("Chap1", "1.1")
bin1.add_right("Chap1", "1.2")
bin1.add_left("Chap2", "2.1")
bin1.add_right("Chap2", "2.2")

#bin1.postorder(bin1.root)
print("------------------")
print("BinaryTree này có trống ko?:", bin1.is_empty())
print("Số phần tử trong BinaryTree:", bin1._len_())
print("Phần tử này có phải root ko:", bin1.is_root("Chap1"))
print("Số lượng Node con của Node này là:", bin1.num_children("Chap1"))
print("Node trái của Node này là:", bin1.left("Chap1"))
print("Node phải của Node này là:", bin1.right("Chap1"))
print("Node cha của Node này là:", bin1._parent_("Chap1"))
print("Node này có phải Externode ko?:", bin1.is_leaf("Chap1"))
        
        
    
    