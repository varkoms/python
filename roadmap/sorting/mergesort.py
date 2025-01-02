import time


def merge(left, right):
    # If the first array is empty, then nothing needs
    # to be merged, and you can return the second array as the result
    if len(left) == 0:
        return right

    # If the second array is empty, then nothing needs
    # to be merged, and you can return the first array as the result
    if len(right) == 0:
        return left

    # Initialize the result array
    result = []

    # Indexes for left and right arrays
    index_left = index_right = 0

    # Loop over the arrays until the result is complete
    while len(result) < len(left) + len(right):
        # If the left array is empty, add the element from the right array
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        # If you reach the end of either array, then you can add the remaining elements from the other array to the result and break the loop
        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break

    return result

def merge_sort(array):
    # If the input array contains fewer than two elements, return it as the result
    if len(array) < 2:
        return array

    midpoint = len(array) // 2

    # Sort the array by recursively splitting the input into two equal halves, sorting each half and merging them together into the final result
    return merge(
        left=merge_sort(array[:midpoint]),
        right=merge_sort(array[midpoint:])
    )

# Example usage

start_time = time.process_time()
array = [8, 2, 6, 4, 5]
print(merge_sort(array))  # Output: [2, 4, 5, 6, 8]
print("Execution time: %s seconds" % (time.process_time() - start_time))

# Strengths of Merge Sort
# 1. It's efficient for large data sets
# 2. It's efficient for lists that are mostly sorted
# 3. It's a stable sort, meaning it preserves the order of equal elements in the sorted list

# Weaknesses of Merge Sort
# 1. It's less efficient in practice than other quadratic algorithms for small data sets
# 2. It's more complex to implement than other quadratic algorithms like bubble sort and insertion sort
# 3. It requires additional memory space for the temporary arrays used in the merging step
