

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1
        
    def print_list(self):
        cur_head = self.head
        while cur_head is not None:
            print(cur_head.value)
            cur_head = cur_head.next
 
    def append(self, value):
        new_node = Node(value)
        
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else: 
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        
        return True
    
    def prepend(self, value):
        
        new_node = Node(value)
        
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
        
    def pop(self):
        if self.length == 0: return None
        
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp
    
    def pop_first(self):
        if self.length == 0: return None
        
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else: 
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp
    
    def get(self, index):
        if index < 0 or index > self.length-1 : return None
        
        cur_head = self.head
        if index < self.length/2:
            for _ in range(index):
                    cur_head = cur_head.next
        else: 
            cur_head = self.tail
            for _ in range(self.length -1, index, -1):
                cur_head = cur_head.prev
    
        return cur_head
    
    def set_value(self, index, value):        
        replace = self.get(index)
        if replace == None: return None
        
        replace.value = value
        return replace
    
    def insert(self, index, value):
        if self.length == 0:
            self.head.prev = new_node
            new_node = self.head
            self.head = new_node
            
        if index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        else: 
            new_node = Node(value)
            node_at = self.get(index)
            if node_at == None:
                return None
            new_node.next = node_at
            new_node.prev = node_at.prev
            node_at.prev.next = new_node
            node_at.prev = new_node
        self.length +=1
        return new_node
    
    def remove(self, index):
        if index < 0 or index > self.length: return False
        
        if self.length == 1:
            self.head = None
            self.tail = None
        elif index == 0:
            return self.pop_first()
        elif index == self.length:
            return self.pop()
        
        rem_node = self.get(index)
        if rem_node == None: return None
        before = rem_node.prev
        after = rem_node.next
        
        before.next = after
        after.prev = before
        rem_node.prev = None
        rem_node.after = None
        
        self.length -= 1
        return True
                  
    def swap_first_last(self):
        if self.length == 0: return False
        
        head_value = self.head.value
        self.head.value = self.tail.value
        self.tail.value = head_value
        return True
        
    def reverse(self):
        if self.length < 1: return False
        
        prev = None
        curr_head = self.head
        self.tail = self.head
        
        while curr_head:
            next_v = curr_head.next
            curr_head.next = prev
            prev = curr_head
            curr_head = next_v
        
        self.head = prev
        return True
        
myDobule = DoublyLinkedList(1)
myDobule.append(2)
myDobule.append(3)
myDobule.append(3)
myDobule.append(5)


# myDobule.print_list()

# myDobule.pop()
# myDobule.pop_first()


myDobule.print_list()

print("The head: ", myDobule.head.value, " the tail ", myDobule.tail.value)
print("Reveres:")
myDobule.reverse()

print("The head: ", myDobule.head.value, " the tail ", myDobule.tail.value)

myDobule.print_list()