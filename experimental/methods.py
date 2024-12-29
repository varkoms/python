# METHODS HERE
def turn_clockwise(n):
    compass_points = {"N": "E", "E": "S", "S": "W", "W": "N"}
    return compass_points.get(n, None)


def day_name(day_number):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    if 0 <= day_number < len(days):
        return days[day_number]
    else:
        return None

# Define a function named day_add that takes two parameters: day and delta
def day_add(day, delta):
    # Create a list of days of the week
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    # Find the index of the given day in the list
    current_index = days.index(day)
    # Calculate the new index by adding delta to the current index and taking the modulus with the length of the list
    new_index = (current_index + delta) % len(days)
    # Return the day at the new index
    return days[new_index]


def to_secs(hours, minutes, seconds):
    return hours * 3600 + minutes * 60 + seconds


def hours_in(seconds):
    hours = seconds // 3600
    return hours


def f2c(t):
    """
    Convert Fahrenheit to Celsius.

    This function takes a temperature in Fahrenheit and converts it to Celsius,
    rounding the result to the nearest integer.

    Parameters:
    t (float): Temperature in Fahrenheit.

    Returns:
    int: Temperature in Celsius, rounded to the nearest integer.
    """
    return round((t - 32) * 5 / 9)


def is_sorted(lst):
    """
    Check if a list is sorted in ascending order.

    This function takes a list and checks if it is sorted in ascending order.

    Parameters:
    lst (list): List of integers.

    Returns:
    bool: True if the list is sorted in ascending order, False otherwise.
    """
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))


def binary_search(lst, target):
    """
    Perform binary search on a sorted list.

    This function takes a sorted list and a target value, and performs binary
    search to find the index of the target value in the list. If the target
    value is not in the list, the function returns None.

    Parameters:
    lst (list): Sorted list of integers.
    target (int): Value to search for in the list.

    Returns:
    int: Index of the target value in the list, or None if the target value is
         not in the list.
    """
    if (not is_sorted(lst)):
        return "List is not sorted"

    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = lst[mid]

        if guess == target:
            return f"Item found in pos: {mid}"
        elif guess < target:
            low = mid + 1
        else:
            high = mid - 1

    return None


def is_factor(f, n):
    """
    Check if f is a factor of n.

    This function takes two integers, f and n, and checks if f is a factor of n.

    Parameters:
    f (int): Potential factor.
    n (int): Number to check against.

    Returns:
    bool: True if f is a factor of n, False otherwise.
    """
    return n % f == 0

def is_multiple(m, n):
    """
    Check if m is a multiple of n.

    This function takes two integers, m and n, and checks if m is a multiple of n
    by reusing the is_factor function.

    Parameters:
    m (int): Number to check.
    n (int): Potential factor.

    Returns:
    bool: True if m is a multiple of n, False otherwise.
    """
    return is_factor(n, m)

def remove_adjacent_dups(lst):
    """
    Remove adjacent duplicates from a list.

    This function takes a list and removes adjacent duplicates from it, keeping
    only the first occurrence of each element.

    Parameters:
    lst (list): List of elements.

    Returns:
    list: List with adjacent duplicates removed.
    """
    result = []
    most_recent_item = None
    for e in lst:
        if e != most_recent_item:
            result.append(e)
            most_recent_item = e

    return result

def merge_sorted_lists(xs, ys):
    """
    Merge two sorted lists into a single sorted list.
    This function takes two sorted lists, `xs` and `ys`, and merges them into a new list
    that is also sorted. The input lists `xs` and `ys` must be sorted in ascending order.

    Parameters:
    xs (list): The first sorted list.
    ys (list): The second sorted list.

    Returns:
    list: A new sorted list containing all elements from `xs` and `ys`.

    Example:
    >>> merge_sorted_lists([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    """

    i, j = 0, 0
    newlist = []

    while i < len(xs) and j < len(ys):
        if xs[i] < ys[j]:
            newlist.append(xs[i])
            i += 1
        else:
            newlist.append(ys[j])
            j += 1

    # Añadir los elementos restantes de xs o ys
    newlist.extend(xs[i:])
    newlist.extend(ys[j:])

    return newlist

def load_words_from_file(filename):
    """ Read words from filename, return a list of words """
    f = open(filename, "r")
    file_content = f.read()
    f.close()
    wds = file_content.split()
    return wds


def share_diagonal(x0, y0, x1, y1):
    """ Is (x0, y0) on a shared diagonal with (x1, y1)? """
    dy = abs(y1 - y0)
    dx = abs(x1 - x0)
    return dx == dy

def col_clashes(bs, c):
    """ Return True if the queen at column c clashes with any queen to its left """
    for i in range(c):
        if share_diagonal(i, bs[i], c, bs[c]):
            return True
    return False

# END OF METHODS
