def selection_sort(unsorted: list) -> list:

    for i in range(0, len(unsorted) - 1):
        min = i

        for j in range(i + 1, len(unsorted)):
            if unsorted[j] < unsorted[min]:
                min = j

        if min != i:
            unsorted[i], unsorted[min] = unsorted[min], unsorted[i]

    return unsorted


def bubble_sort(unsorted: list) -> list:

    for i in range(0, len(unsorted)):
        for j in range(0, len(unsorted) - 1 - i):
            if unsorted[j] > unsorted[j + 1]:
                unsorted[j], unsorted[j + 1] = unsorted[j + 1], unsorted[j]

    return unsorted


def heapify(arr, n, i): 
    largest = i  
    left_child = 2 * i + 1    
    right_child = 2 * i + 2     
    
    if left_child < n and arr[i] < arr[left_child]: 
        largest = left_child
    
    if right_child < n and arr[largest] < arr[right_child]: 
        largest = right_child
    
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i] 
        heapify(arr, n, largest) 

def heapSort(arr): 
    n = len(arr) 
    # Build a maxheap. 
    for i in range(n//2 - 1, -1, -1): 
        heapify(arr, n, i) 
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0) 
    return arr


