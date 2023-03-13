### List Comprehension ###

my_original_list = [35, 24, 62, 52, 30, 30, 17]

my_list = [i for i in my_original_list]  
print(my_list)  # [35, 24, 62, 52, 30, 30, 17]

my_list = [i for i in range(8)]
print(my_list)  # [0, 1, 2, 3, 4, 5, 6, 7]

my_list = [i + 1 for i in range(8)]
print(my_list)  # [1, 2, 3, 4, 5, 6, 7, 8]

my_list = [i * 2 for i in range(8)]
print(my_list)  # [0, 2, 4, 6, 8, 10, 12, 14]

my_list = [i * i for i in range(8)]
print(my_list)  # [0, 1, 4, 9, 16, 25, 36, 49]