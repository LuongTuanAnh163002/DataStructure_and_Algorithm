#Function 7: Xóa một node trong BinarySearchTree, lưu ý do code gốc không thể xóa hết tất cả các phần tử trong cây
#bởi vì khi binary search tree có dạng linklist vd: 1 -> 2 -> 3 -> 4 nghiêng về hẳn bên trái hoặc phải thì code sẽ không thể xóa được node gốc nên
#tôi đã bổ sung một số điểm để có thể xóa hết được tất cả các thành phần trong cây

from collections import deque 
class Node:
    def __init__(self, element):
        self.element = element
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0
        self.total = 0
        
    def is_empty(self): #1: kiểm tra xem tree có trống không
        return self.size == 0
    
    def _count_(self): #2: Trả về số node có trong tree
        return self.size
    
    def _sum_(self): #3: Trả về tổng số giá trị của tất cả các node có trong tree
        return self.total
    
    def average(self): #4: Trả về trung bình cộng giá trị của tất cả các node có trong tree
        if self.size == 0:
            return "0/0 = None"
        else:
            return self.total / self.size
    
    def add_root(self, val): #hàm bổ trợ: Thêm node gốc
        new_node = Node(val)
        if self.root is not None:
            print("Root in tree is exist")
        else:
            self.root = new_node
            self.size += 1
            self.total += val
    
    def insert(self, tmp, val): #5: Thêm 1 node mới vào tree
        if val == tmp.element:
            return
        elif val < tmp.element:
            if tmp.left:
                self.insert(tmp.left, val)
            else:
                tmp.left = Node(val)
                self.size += 1
                self.total += val
        else:
            if tmp.right:
                self.insert(tmp.right, val)
            else:
                tmp.right = Node(val)
                self.size += 1
                self.total += val
    
    def search(self, tmp, val): #6: Kiểm tra xem một giá trị có nằm trong tree hay không
        if self.size != 0:
            if val == tmp.element:
                return True
            elif val < tmp.element and tmp.left != None:
                return self.search(tmp.left, val)
            elif val > tmp.element and tmp.right != None:
                return self.search(tmp.right, val)
            else:
                return False
        else:
            return "Tree do not have any Node to search"
    
    def clear(self): #7: Xóa toàn bộ Node trong tree
        self.root = None
        self.size = 0
        self.total = 0
    
    
    def delete(self, p, val): #8: Xóa một node trong BinarySearchTree, lưu ý do code gốc không thể xóa hết tất cả các phần tử trong cây
    #bởi vì khi binary search tree có dạng linklist vd: 1 -> 2 -> 3 -> 4 nghiêng về hẳn bên trái hoặc phải thì code sẽ không thể xóa được node gốc nên
    #tôi đã bổ sung một số điểm để có thể xóa hết được tất cả các thành phần trong cây
        if self.size == 1:
            self.clear()
            return
        if p is None:
            return p
        
        if val < p.element:
            p.left = self.delete(p.left, val)
        
        elif val > p.element:
            p.right = self.delete(p.right, val)
        
        else:
            if val == self.root.element and self.root.right is None and self.root.left is not None: #Xóa node gốc trong TH cây nghiêng hoàn toàn sang trái
                tmp = self.root.left
                self.root = tmp
                self.size -= 1
                self.total -= val
                
            elif val == self.root.element and self.root.left is None and self.root.right is not None:#Xóa node gốc trong TH cây nghiêng hoàn toàn sang phải
                tmp = self.root.right
                self.root = tmp
                self.size -= 1
                self.total -= val
            
            elif p.left is None:
                tmp = p.right
                p = None
                return tmp
            
            elif p.right is None:
                tmp = p.left
                p = None
                return tmp
            
            else:
                min_value = self.find_min(p.right)
                p.element = min_value
                p.right = self.delete(p.right, min_value)
        
        if p.element == self.root.element:
            self.size -= 1
            self.total -= val
        
        return p
                
    def preorder(self, tmp): #9: Duyệt hêt tất cả các phần tử trong tree theo: root -> left -> right
        if tmp:
            print(tmp.element, end = " ")
            if tmp.left:
                self.preorder(tmp.left)
            if tmp.right:
                self.preorder(tmp.right)
        else:
            print("Tree do not have any Node to traverse")
    
    def postorder(self, tmp): #10: Duyệt hết tất cả các phần tử trong tree theo: left -> right -> root
        if tmp:
            if tmp.left:
                self.postorder(tmp.left)
            if tmp.right:
                self.postorder(tmp.right)
            print(tmp.element, end = " ")
        else:
            print("Tree do not have any Node to traverse")
            
    def inorder(self, tmp): #11: Duyệt hết tất cả các phần tử trong tree theo: left -> root -> right
        if tmp:
            if tmp.left:
                self.inorder(tmp.left)
            print(tmp.element, end = " ")
            if tmp.right:
                self.inorder(tmp.right)
        else:
            print("Tree do not have any Node to traverse")
    
    def breadth(self, tmp): #12: Duyệt hết tất cả các phần tử trong tree theo thứ tự từ trên xuống dưới
        if tmp:
            queue = deque()
            queue.append(self.root)
            while len(queue) != 0:
                p = queue.popleft()
                print(p.element, end = " ")
                for i in [p.left, p.right]:
                    if i is not None:
                        queue.append(i)
        else:
            print("Tree do not have any Node to traverse")
    
        
    def find_max(self, tmp): #13: Tìm GTLN trong tree
        if self.size != 0:
            if tmp.right is None:
                return tmp.element
            else:
                return self.find_max(tmp.right)
        else:
            return "Tree is not exist Max value"
        
    def find_min(self, tmp): #14: Tìm GTNN trong tree
        if self.size != 0:
            if tmp.left is None:
                return tmp.element
            else:
                return self.find_min(tmp.left)
        else:
            return "Tree is not exist Min value"
        
    def get_height(self, tmp): #15: Tính độ cao của tree
        if tmp is None:
            return 0
        else:
            lheight = rheight = 1
            if tmp.left:
                lheight += self.get_height(tmp.left)
                
            if tmp.right:
                rheight += self.get_height(tmp.right)
            
            return max(lheight, rheight)
    
    def get_node(self, tmp, ele): #Hàm bổ trợ
        if tmp.element == ele:
            return tmp
         
        for i in [tmp.left, tmp.right]:
            if i:
                a = self.get_node(i, ele)
                if a == None:
                    continue
                else:
                    return a
    
    def is_balanced(self, p): #Hàm bổ trợ
        a = self.get_height(p.right)
        b = self.get_height(p.left)
        ans = a - b
        if ans >= -1 and ans <= 1:
            return True
        else:
            return False
        
    def Tree_is_AVL(self, tmp): #16: kiểm tra xem tree có phải là AVLtree không
        if tmp:
            a = deque()
            a.append(self.root)
            b = []
            while len(a) != 0:
                p = a.popleft()
                b.append(p.element)
                for i in [p.left, p.right]:
                    if i is not None:
                        a.append(i)
            for i in b:
                c = self.get_node(self.root, i)
                if self.is_balanced(c) == False:
                    return False
            return True
        else:
            return "Tree do not have any Node to check"
        
BStree = BinarySearchTree()
data = [8,13,2,6,7,10,15,1,5,16,17,3]
BStree.add_root(data[0])
for i in data[1:]:
    BStree.insert(BStree.root, i)
print("--------------Insert 8 node to Binary search tree-------------------")
print("Preorder traverse:")
BStree.preorder(BStree.root)
 
print("\nPostorder traverse:")
BStree.postorder(BStree.root)

print("\nInorder traverse:")
BStree.inorder(BStree.root)

print("\nFirst breadth traverse:")
BStree.breadth(BStree.root)

print("\nTree is empty:", BStree.is_empty())
print("The number of Node:", BStree._count_())
print("The Sum:", BStree._sum_())
print("The Average:", BStree.average())
print("Min:", BStree.find_min(BStree.root))
print("Max:", BStree.find_max(BStree.root))
print("Height of tree:", BStree.get_height(BStree.root))
print("10 in Tree:", BStree.search(BStree.root, 10))
print("Tree is AVL:", BStree.Tree_is_AVL(BStree.root))

 
print("------------After delete one Node with value 10--------------")
BStree.delete(BStree.root, 10)
print("Preorder traverse:")
BStree.preorder(BStree.root)

print("\nPostorder traverse:")
BStree.postorder(BStree.root)

print("\nInorder traverse:")
BStree.inorder(BStree.root)

print("\nFirst breadth traverse:")
BStree.breadth(BStree.root)
print("\nTree is empty:", BStree.is_empty())
print("The number of Node:", BStree._count_())
print("The Sum:", BStree._sum_())
print("The Average:", BStree.average())
print("Min:", BStree.find_min(BStree.root))
print("Max:", BStree.find_max(BStree.root))
print("Height of tree:", BStree.get_height(BStree.root))
print("10 in Tree:", BStree.search(BStree.root, 10))
print("Tree is AVL:", BStree.Tree_is_AVL(BStree.root))

print("------------After delete all Node--------------")
BStree.clear()
print("Preorder traverse:")
BStree.preorder(BStree.root)

print("\nPostorder traverse:")
BStree.postorder(BStree.root)

print("\nInorder traverse:")
BStree.inorder(BStree.root)

print("\nFirst breadth traverse:")
BStree.breadth(BStree.root)

print("\nTree is empty:", BStree.is_empty())
print("The number of Node:", BStree._count_())
print("The Sum:", BStree._sum_())
print("The Average:", BStree.average())
print("Min:", BStree.find_min(BStree.root))
print("Max:", BStree.find_max(BStree.root))
print("Height of tree:", BStree.get_height(BStree.root))
print("10 in Tree:", BStree.search(BStree.root, 10))
print("Tree is AVL:", BStree.Tree_is_AVL(BStree.root))

print("----------After delete all, then add 3 node 8, 9, 10----------------")
data = [9, 8, 10]
BStree.add_root(data[0])
for i in data[1:]:
    BStree.insert(BStree.root, i)
print("Preorder traverse:")
BStree.preorder(BStree.root)

print("\nPostorder traverse:")
BStree.postorder(BStree.root)

print("\nInorder traverse:")
BStree.inorder(BStree.root)

print("\nFirst breadth traverse:")
BStree.breadth(BStree.root)

print("\nTree is empty:", BStree.is_empty())
print("The number of Node:", BStree._count_())
print("The Sum:", BStree._sum_())
print("The Average:", BStree.average())
print("Min:", BStree.find_min(BStree.root))
print("Max:", BStree.find_max(BStree.root))
print("Height of tree:", BStree.get_height(BStree.root))
print("10 in Tree:", BStree.search(BStree.root, 10))
print("Tree is AVL:", BStree.Tree_is_AVL(BStree.root))


        