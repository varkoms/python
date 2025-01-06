import calculations

# Importing the functions from the calculations module using * symbol is not a good programming practice. This can lead to duplicate definitions for an identifier. It also hampers the readabilityu of the code. It is better to import the functions individually.
# from calculations import *

print(calculations.add(1, 2))  # 3
print(calculations.subtract(1, 2))  # -1
print(calculations.multiply(1, 2))  # 2
print(calculations.divide(1, 2))  # 0.5
print(calculations.divideInt(1, 2))  # 0

print(dir(calculations))  # ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add', 'divide', 'divideInt', 'multiply', 'subtract']
