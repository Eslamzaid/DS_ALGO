

class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def _left_child(self, index):
        return 2 * index + 1
    
    def _right_child(self, index):
        return 2 * index + 2
    
    def _parent(self, index):
        return (index - 1) // 2
    
    def _swap(self, ind1, ind2):
        first_value = self.heap[ind1]
        self.heap[ind1] = self.heap[ind2]
        self.heap[ind2] = first_value
        
    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1
        
        while current > 0 and \
                self.heap[current] > self.heap[self._parent(current)]:
                    
            self._swap(current, self._parent(current))
            current = self._parent(current)
        return True
    
    def remove(self):
        if len(self.heap) == 0:
            return None
        elif len(self.heap) == 1:
            return self.heap.pop()
        
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        return max_value
    
    def _sink_down(self, index):
        max_index = index
        leng = len(self.heap)
        
        while True:
            left_child = self._left_child(max_index)
            right_child = self._right_child(max_index)
            
            if (left_child < leng) and self.heap[index] < self.heap[left_child]:
                max_index = left_child
                
            if (right_child < leng) and self.heap[max_index] < self.heap[right_child]:
                max_index = right_child
            
            if index != max_index:
                self._swap(index, max_index)
                index = max_index
            else: 
                break
        return                
                
            
heap = MaxHeap()

heap.insert(53)
heap.insert(44)
heap.insert(42)
heap.insert(99)

print(heap.heap)

heap.insert(100)
heap.insert(17)
heap.insert(48)

print(heap.heap)
