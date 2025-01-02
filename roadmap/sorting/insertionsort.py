import time


def insertion_sort(array):
    # Loop from the second element of the array until the end
    for i in range(1, len(array)):
        # This is the element we want to position in its
        # correct place
        key_item = array[i]

        # Initialize the variable that will be used to
        # find the correct position of the element referenced
        j = i - 1

        # Run through the list of items (the left portion
        # of the array) and find the correct position of the
        # element referenced above (the key item)
        # Do this only if the key item is smaller than its
        # adjacent values.
        while j >= 0 and array[j] > key_item:
            # Shift the value one position to the left
            # and reposition j to point to the next element
            # (from right to left)
            array[j + 1] = array[j]
            j -= 1

        # When you finish shifting the elements, you can position
        # the key item in its correct location
        array[j + 1] = key_item

    return array


# Usage
start_time = time.process_time()
array = [8, 2, 6, 4, 5]
print(insertion_sort(array))  # Output: [2, 4, 5, 6, 8]
print("Execution time: %s seconds" % (time.process_time() - start_time))

# Strengths of Insertion Sort
# 1. It's efficient for small data sets
# 2. It's more efficient in practice than other quadratic algorithms like bubble sort and selection sort
# 3. It's simple to implement

# Weaknesses of Insertion Sort
# 1. It's inefficient for large data sets
# 2. It's inefficient for lists that are mostly sorted
# 3. It's inefficient for lists that are sorted in reverse order
