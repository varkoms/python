'''
Shell Sort involves sorting elements which are away from each other. We sort a large sublist of a given list and go on reducing the size of the list until all elements are sorted. The below program finds the gap by equating it to half of the length of the list size and then starts sorting all elements in it. Then we keep resetting the gap until the entire list is sorted.
'''

def shell_sort(input_list, n):
    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = input_list[i]
            j = i
            while j >= interval and input_list[j - interval] > temp:
                input_list[j] = input_list[j - interval]
                j -= interval
            
            input_list[j] = temp
        interval //= 2

list = [19,2,31,45,30,11,121,27]
shell_sort(list, len(list))
print(f'Sorted array in ascending order: {list}') # Sorted array in ascending order: [2, 11, 19, 27, 30, 31, 45, 121]