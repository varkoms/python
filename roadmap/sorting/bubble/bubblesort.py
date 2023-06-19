'''
BUBBLE SORT

It is a comparison-based algorithm in which each pair of adjacent elements is compared and the elements are swapped if they are not in order.
'''

def bubble_sort(list):
    # Swap the elements to arrange in order
    for item_num in range(len(list) -1, 0, -1):
        for idx in range(item_num):
            if list[idx] > list[idx + 1]:
                temp = list[idx]
                list[idx] = list[idx + 1]
                list[idx + 1] = temp

list = [19, 2, 31, 45, 6, 11, 121, 27]
bubble_sort(list)
print(list) # [2, 6, 11, 19, 27, 31, 45, 121]