full_name = lambda first, last : f'Full name: {first.title()} {last.title()}'
print(full_name('Guido', 'Mista')) # Full name: Guido Mista

# Lambda functions are frequently used with higher-order functions, which take one or more functions as arguments or return one or more functions.

high_ord_func = lambda x, func: x + func(x)
print(high_ord_func(2, lambda x: x + x)) # 6
print(high_ord_func(2, lambda x: x + 3)) # 7
