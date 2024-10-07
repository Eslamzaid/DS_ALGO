

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
        
# class Stack:
#     ## Arrays can be better than linked-lists in terms of stack, 
#     # Arrays characteristics :
#         # appened: O(1), read: O(1), pop: O(1), insert: O(N), delete: O(N)
#     def __init__(self, value):
#         new_node = Node(value)
#         self.top = new_node
#         self.height = 1
        
#     def print_stack(self):    
#         cur_node = self.top
#         while cur_node:
#             print(cur_node.value)
#             cur_node = cur_node.next
        
#     def push(self, value):
#         new_node = Node(value)
        
#         if self.height == 0:
#             self.top = new_node
#         else:
#             new_node.next = self.top
#             self.top = new_node
#         self.height += 1
#         return new_node
    
#     def pop(self):
        
#         if self.height == 0: return False
        
#         rem_node = self.top
#         self.top = self.top.next
#         rem_node.next = None
#         self.height -= 1
        
#         return rem_node
        
    
# myStack = Stack(17)
# myStack.print_stack()


class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()

        
def is_balanced_parentheses(the_string):
    check_stack = Stack()
    
    bal_len = len(the_string)
    for i in range(bal_len):
        if the_string[i] == ')':
            ret_val = check_stack.pop()
            if ret_val == None: return False
            elif ret_val == ')': return False
        else: check_stack.push(the_string[i])
    
    if check_stack.size() != 0: return False
    return True    
    
print(is_balanced_parentheses("("))