class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size
        
    
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
            
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)
            
    def set_item(self, key, value):
        index = self.__hash(key)

        if self.data_map[index] == None:
            self.data_map[index] = []
        
        self.data_map[index].append([key, value])
        return True
    
    def get_item(self, key):
        index = self.__hash(key)
        
        if self.data_map[index] is None: return None
        
        for val in self.data_map[index]:
            if val[0] == key:
                return [val[0], val[1]]
            
        return None
        
    def keys(self):
        keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is None:
                continue
            for val in self.data_map[i]:
                keys.append(val[0])
            
        return keys


def item_in_common(li1, li2):
    myObj = {}
    for i in range(len(li1)):
        myObj[li1[i]] = True

    for i in range(len(li2)):
        if li2[i] in myObj:
            return True
    return False

l1 = [1, 3, 5]
l2 = [2, 9, 5]

print(item_in_common(l1, l2))

my_hash_table = HashTable()

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)

my_hash_table.print_table()



"""
    EXPECTED OUTPUT:
    ----------------
    0 :  None
    1 :  None
    2 :  None
    3 :  None
    4 :  [['bolts', 1400], ['washers', 50]]
    5 :  None
    6 :  [['lumber', 70]]

"""