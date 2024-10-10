
big_test = [48, 22, 93, 17, 90, 42, 38, 32, 77, 40, 67, 69, 85, 71, 57, 60, 64, 70, 51,
      22, 24, 90, 32, 45, 82, 38, 61, 84, 26, 33, 39, 38, 86, 34, 59, 74, 7, 88, 
      98, 41, 83, 12, 64, 10, 20, 97, 11, 42, 64, 29, 30, 23, 2, 73, 37, 45, 7,
      80, 88, 25, 84, 25, 7, 39, 53, 73, 96, 62, 25, 82, 33, 51, 60, 68, 7, 99,
      11, 16, 46, 57, 22, 48, 39, 85, 77, 23, 92, 95, 97, 87, 47, 92, 17, 94, 
      15, 76, 30, 72, 28, 95]
test_small = [15, 76, 30, 72, 28, 95]


def merge(array1, array2):
    combined = []
    i = 0
    j = 0
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            combined.append(array1[i])
            i += 1
        else:
            combined.append(array2[j])
            j += 1
              
    while i < len(array1):
        combined.append(array1[i])
        i += 1

    while j < len(array2):
        combined.append(array2[j])
        j += 1

    return combined


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    middle_ind = int(len(arr)/2)
    left = merge_sort(arr[:middle_ind])
    right = merge_sort(arr[middle_ind:])
    
    return merge(left, right)

my_list = merge_sort(big_test)
print(my_list)