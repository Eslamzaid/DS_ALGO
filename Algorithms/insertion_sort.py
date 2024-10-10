
big_test = [48, 22, 93, 17, 90, 42, 38, 32, 77, 40, 67, 69, 85, 71, 57, 60, 64, 70, 51,
      22, 24, 90, 32, 45, 82, 38, 61, 84, 26, 33, 39, 38, 86, 34, 59, 74, 7, 88, 
      98, 41, 83, 12, 64, 10, 20, 97, 11, 42, 64, 29, 30, 23, 2, 73, 37, 45, 7,
      80, 88, 25, 84, 25, 7, 39, 53, 73, 96, 62, 25, 82, 33, 51, 60, 68, 7, 99,
      11, 16, 46, 57, 22, 48, 39, 85, 77, 23, 92, 95, 97, 87, 47, 92, 17, 94, 
      15, 76, 30, 72, 28, 95]
test_small = [15, 76, 30, 72, 28, 95]


def insertion_sort(arr):
    
    for i in range(1, len(arr)):
        
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                temp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = temp
            else: 
                break         
    return arr 

## Other:
# def insertion_sort(arr):
#   for i in range(1, len(arr)):
#        key = arr[i]
#        j = i - 1
#        while j >= 0 and arr[j] > key:
#             arr[j + 1] = arr[j]
#            j -= 1
#        arr[j + 1] = key


print(insertion_sort(test_small))
print("<----------- Big test -------------->")
print(insertion_sort(big_test))