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

# END OF METHODS
