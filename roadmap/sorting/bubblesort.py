import time


def bubble_sort(array):
    n = len(array)

    for i in range(n):
        # Create a flag that will allow the function to
        # terminate early if there's nothing left to sort
        already_sorted = True

        """
        Start looking at earch item of the list one by one,
        comparing it with its adjacent value. With each iteration, the portion of the array that you look at
        shrinks because the remaining items have already been sorted.
        """
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                # If the item you're looking at is greater than its adjacent value, then swap them
                array[j], array[j + 1] = array[j + 1], array[j]

                # Since you had to swap two elements, set the already_sorted flag to False so the algorithm doesn't finish prematurely
                already_sorted = False

        # If there were no swaps during the last iteration,
        # the array is already sorted, and you can terminate
        if already_sorted:
            break

    return array

# Example usage
start_time = time.process_time()
array = [5, 4, 3, 2, 1]
print(bubble_sort(array))  # Output: [1, 2, 3, 4, 5]
print("Execution time: %s seconds" % (time.process_time() - start_time))

# Advantages of Bubble Sort
# 1. It's simple to understand and implement
# 2. It's easy to implement in a way that it will sort the list in place
# 3. It's efficient for small lists

# Disadvantages of Bubble Sort
# 1. It's inefficient for large lists
# 2. It's inefficient for nearly sorted lists
# 3. It's inefficient for reverse-ordered lists
# 4. It's inefficient for lists that are sorted in the reverse order
