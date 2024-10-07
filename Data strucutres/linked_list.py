class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
        
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1   
        return True  

    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        
        if index == 0:
            return self.pop_first()
            
        if index == self.length:
            return self.pop()
        
        before = self.get(index-1)
        after = before.next.next
        rem = before.next
        
        before.next = after
        
        self.length -= 1
        return rem
        
    def reverse(self):
        if self.length <= 0: return None
            
        next_v = self.head
        end = self.tail
        
        i = 1 
        while i < int(self.length/2):
            temp = next_v.value
            next_v.value = end.value
            end.value = temp
            
            next_v = next_v.next
            end = self.get(self.length-(i+1))
            
            i+= 1

    def find_middle_node(self):
        if self.head == None: return None
        
        slow = self.head.next
        if slow == None: 
            return self.head
        fast = self.head.next.next
        while 1:
            if fast == None or fast.next == None:
                return slow
            print("HI")
            
            if fast.next == None:
                return slow
                
            else:
                fast = fast.next.next
                slow = slow.next
                
    def has_loop(self):
        if self.length <= 0 : return False
        if self.tail.next is not None: return True
        
        slow = self.head.next
        if slow == None:
            return False
        fast = self.head.next.next
        while slow is not None:
            if slow == fast:
                return True
                
            if fast == None or fast.next is None:
                return False
            print("The slow ", slow.value, " The fast ", fast.value)
            slow = slow.next
            fast = fast.next.next