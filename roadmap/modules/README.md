# Module

## What is a Python Module?

A Python module is a file containing Python definitions and statements. A module can define functions, classes, and variables. A module can also include runnable code. Grouping related code into a module makes the code easier to understand and use. It also makes the code logically organized.

# Python Import From Module

Python’s from statement lets you import specific attributes from a module without importing the module as a whole.

## Import Specific Attributes from a Python module

Here, we are importing specific sqrt and factorial attributes from the math module.

```python
# importing sqrt() and factorial from the
# module math
from math import sqrt, factorial

# if we simply do "import math", then
# math.sqrt(16) and math.factorial()
# are required.
print(sqrt(16))
print(factorial(6))
```

Output:

```zsh
4.0
720
```
