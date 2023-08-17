'''
Insertion sort involves finding the right place for a given element in a sorted list. So in beginning we compare the first two elements and sort them by comparing them. Then we pick the third element and find its proper position among the previous two sorted elements. This way we gradually go on adding more elements to the already sorted list by putting them in their proper position.
'''

def insertion_sort(arr):
    if (n := len(arr)) <= 1:
        return
    for i in range(1, n):
        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j] :
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

list = [19,2,31,45,30,11,121,27]
insertion_sort(list)
print(list) # [2, 11, 19, 27, 30, 31, 45, 121]