from random import randint
import time
from tracemalloc import start

def quicksort(array):
    # If the input array contains fewer than 2 elements, return it as the result of the function
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    # Select your `pivot` element randomly
    pivot = array[randint(0, len(array) - 1)]

    for item in array:
        # Elements that are smaller than the `pivot` go to the `low` list. Elements that are highter go to the `high` list. Elements that are equal to `pivot` go to the `same` list.
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    # The final result combines the sorted 'low' list
    # with the 'same' list and the sorted 'high' list
    return quicksort(low) + same + quicksort(high)


# Example usage
start_time = time.process_time()
array = [8, 2, 6, 4, 5]
result = quicksort(array)
print(result)  # Output: [2, 4, 5, 6, 8]
end_time = time.process_time()

print("quicksort({0}) = {1}, ({2:.2f} secs)".format(array, result, end_time-start_time))

# Strenghts of quicksort:
# - Quicksort is an efficient sorting algorithm with an average time complexity of O(n log n).
# - Quicksort is an in-place sorting algorithm, meaning it doesn't require any extra storage.
# - Quicksort is a divide-and-conquer algorithm, which means that it breaks the problem into smaller sub-problems and solves them recursively.

# Weaknesses of quicksort:
# - Quicksort is not a stable sorting algorithm, meaning that the relative order of equal sort items is not preserved.
# - Quicksort has a worst-case time complexity of O(n^2) when the pivot element is the smallest or largest element in the list.
# - Quicksort is not a good choice for small lists because it has a high constant factor and can be outperformed by other algorithms for small inputs.
