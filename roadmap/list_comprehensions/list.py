# Without list comprehension you will have to write a for
# statement with a conditional test inside.

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_list = []

for x in fruits:
    if "a" in x:
        new_list.append(x)
  
print(new_list) # ['apple', 'banana', 'mango']

# With list comprehension you can do all that with only one line of code:

new_list = [x for x in fruits if "a" in x]
print(new_list) # ['apple', 'banana', 'mango']