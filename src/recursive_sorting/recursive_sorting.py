# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    for i in range(elements):
        if (len(arrA) > 0 and len(arrB) > 0):
            merged_arr[i] = arrA.pop(0) if arrA[0] < arrB[0] else arrB.pop(0)
        elif len(arrA) == 0:
            merged_arr[i] = arrB.pop(0)
        else:
            merged_arr[i] = arrA.pop(0)
    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) > 1:
        left = arr[0:len(arr)//2]
        right = arr[len(arr)//2:]
        return merge(merge_sort(left), merge_sort(right))
    else:
        return arr
    return arr

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO
    while start < end:
        if arr[start] < arr[mid]:
            start += 1
        else:
            arr.insert(start, arr.pop(mid))
            start += 1
            mid += 1
    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
