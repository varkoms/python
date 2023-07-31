from random import randint

def quicksort(array):
    # If the input array contains fewer than two elements;
    # then return it as the result of the function
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    # Select your 'pivot' element
    pivot = array[randint(0, len(array) - 1)]

    for item in array:
        # Elements that are smaller than the 'pivot' go to
        # the 'low' list. Elements that are larger than
        # 'pivot' go to the 'high' list. Elements that are
        # equal to 'pivot' go to the 'same' list.
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    return quicksort(low) + same + quicksort(high)

list = [8, 2, 6, 4, 5]
print(quicksort(list)) # [2, 4, 5, 6, 8]
            