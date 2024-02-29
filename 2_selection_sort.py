def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    new_Arr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        new_Arr.append(arr.pop(smallest))
    return new_Arr

print selectionSort([12,123,0,11,1])