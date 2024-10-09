

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def contains(self, value):
        
        if self.root is None: return False
        
        cur_node = self.root
        while cur_node:
            if cur_node.value == value:
                return True
            elif value < cur_node.value:
                if cur_node.left is None:
                    return False
                cur_node = cur_node.left
            else:
                if cur_node.right is None:
                    return False
                cur_node = cur_node.right
        
        return False
    
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: 
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right               

    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        if current_node.value == value:
            return True
        
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)
        else: 
            return self.__r_contains(current_node.left, value)    
    
    def r_contains(self, value):
        return self.__r_contains(self.root, value)
    
    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)
        elif value > current_node.value:
            current_node.left = self.__r_insert(current_node.right, value)
        else: 
            current_node.right = self.__r_insert(current_node.left, value)
        return current_node
        
    def r_insert(self, value):
        if self.root == None:
            self.root = Node(value)
        return self.__r_insert(self.root, value)
    
    
    def min_value(self, current_node):
        while current_node.left is not None:
            current_node =current_node.left
        return current_node.value
            
    
    def __delete(self, current_node, value):
        if current_node == None:
            return None
        if value > current_node.value:
            current_node.right = self.__delete(current_node.right, value)
        if value < current_node.value:
            current_node.left = self.__delete(current_node.left, value)
        else:
            if current_node.left is None and current_node.right is None:
                return None
            elif current_node.left is None:
                return current_node.left
            elif current_node.right is None:
                return current_node.right
            else:
                minim_value = self.min_value(current_node.right)
                current_node.value = minim_value
                current_node.right = self.__delete(current_node.right, minim_value)
        return current_node
    
    def r_delete(self, value):
        return self.__r_delete(self.root, value)
    
    
    def Breadth_first_search(self):
        queue = []
        result = []
        current_node = self.root
        
        # [(15)]
        queue.append(current_node)
        
        while len(queue) > 0:
            current_node = queue.pop(0)
            result.append(current_node.value)
            
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)         
                
        return result  


    def Depth_first_search_PreOrder(self):
        result = []
        current_node = self.root
        
        def traverse(current_node):
            result.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
                
        return result    
    
    def Depth_first_search_PostOrder(self):
        result = []
        current_node = self.root      
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            result.append(current_node.value)
        traverse(self.root)
                
        return result    


    def Depth_first_search_InOrder(self):
        result = []
        current_node = self.root      
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            result.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
                
        return result    

    
    
    
    
def check(expect, actual, message):
    print(message)
    print("EXPECTED:", expect)
    print("RETURNED:", actual)
    print("PASS" if expect == actual else "FAIL", "\n")

# print("\n----- Test: Insert to Empty Tree -----\n")
# bst = BinarySearchTree()
# result = bst.insert(5)
# check(True, result, "Insert 5, should succeed:")
# check(5, bst.root.value, "Root value after inserting 5:")
# check(None, bst.root.left, "Root's left child after inserting 5:")
# check(None, bst.root.right, "Root's right child after inserting 5:")

print("\n----- Test: Insert to Existing Tree -----\n")
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(2)
bst.insert(1)
bst.insert(15)
print(bst.Depth_first_search_PreOrder())
print(bst.Depth_first_search_PostOrder())
print(bst.Depth_first_search_InOrder())
print(bst.Breadth_first_search())
# result = bst.insert(3)
# check(True, result, "Insert 3, should succeed:")
# check(3, bst.root.left.left.value, "Root's left-left value after inserting 3:")
# check(None, bst.root.left.left.left, "Root's left-left-left child after inserting 3:")
# check(None, bst.root.left.left.right, "Root's left-left-right child after inserting 3:")

# print("\n----- Test: Insert Duplicate Value -----\n")
# bst = BinarySearchTree()
# bst.insert(10)
# bst.insert(5)
# result = bst.insert(5)
# check(False, result, "Insert 5 again, should fail:")
# check(None, bst.root.left.left, "Root's left-left child after inserting 5 again:")
# check(None, bst.root.left.right, "Root's left-right child after inserting 5 again:")

# print("\n----- Test: Insert Greater Than Root -----\n")
# bst = BinarySearchTree()
# bst.insert(10)
# result = bst.insert(15)
# check(True, result, "Insert 15, should succeed:")
# check(15, bst.root.right.value, "Root's right value after inserting 15:")
# check(None, bst.root.right.left, "Root's right-left child after inserting 15:")
# check(None, bst.root.right.right, "Root's right-right child after inserting 15:")

# print("\n----- Test: Insert Less Than Root -----\n")
# bst = BinarySearchTree()
# bst.insert(10)
# result = bst.insert(5)
# check(True, result, "Insert 5, should succeed:")
# check(5, bst.root.left.value, "Root's left value after inserting 5:")
# check(None, bst.root.left.left, "Root's left-left child after inserting 5:")
# check(None, bst.root.left.right, "Root's left-right child after inserting 5:")

