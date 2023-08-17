# Import module in Python
"""
We can import the functions, and classes defined in a module to another module using the import statement in some other Python source file.

When the interpreter encounters an import statement, it imports the module if the module is present in the search path. A search path is a list of directories that the interpreter searches for importing a module. For example, to import the module calc.py, we need to put the following command at the top of the script.
"""

# Importing module calc.py
import calc

print(calc.add(10, 2)) # 12

# Renaming the Python module
# We can rename the module while importing it using the keyword.

# importing sqrt() and factorial from the
# module math
import math as mt

# if we simply do "import math", then
# math.sqrt(16) and math.factorial()
# are required.
print(mt.sqrt(16)) # 4.0
print(mt.factorial(6)) # 720