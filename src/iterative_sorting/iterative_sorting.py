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
    # If array length is 1 or less return array
    if len(arr) <= 1:
        return arr
    # If the array contains negative values return error message
    if min(arr) < 0:
        return "Error, negative numbers not allowed in Count Sort"
    # Create an array with values 0 to max(arr) to store the counts
    counts = [0 for i in range(max(arr) + 1)]
    # Fill in the count for each value
    for i in arr:
        counts[i] += 1
    # Generate results array
    results = []
    for i in range(len(counts)):
        results.extend([i] * counts[i])
    return results

# Wikipedia code
def count_sort_wikipedia(arr):
    count = [0 for i in range(max(arr) + 1)]
    for i in arr:
        count[i] += 1

    total = 0
    for i in range(len(count)):
        count[i], total = total, count[i] + total

    output = [None] * len(arr)
    for i in arr:
        output[count[i]] = i
        count[i] += 1

    return output

print(count_sort_wikipedia([5, 3, 1, 8, 9, 100]))