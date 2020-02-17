# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    for i in range (0, len(arr) - 1):
        current_index = i
        smallest_index = i
        for j in range (i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        if current_index != smallest_index:
            arr[current_index], arr[smallest_index] = arr[smallest_index], arr[current_index]
    return arr

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    while True:
        swaps = 0
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swaps += 1
        if swaps == 0:
            break
    return arr

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):
    
    return arr

arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

print(count_sort(arr1))