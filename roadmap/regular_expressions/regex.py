'''
Regular expressions are a powerful language for matching text patterns. This page gives a basic introduction to regular expressions themselves sufficient for our Python exercises and shows how regular expressions work in Python. The Python "re" module provides regular expression support.'''

import re

def match(pattern, string):
  match = re.search(pattern, string)
  # If-statement after search() test if it succeeded
  if match:
    result = match.group()
    return f'found {result}'
  else:
    return 'Did not find :('

pattern = r'word:\w\w\w'
str = 'an example word:cat!!'
result = match(pattern, str)
print(result)

# Basic Examples
# Search for pattern 'iii' in string 'piiig'
# All of the pattern must match, but it may appear anywhere.
# On success, match.group() is matched text.
print(match(r'iii', 'piiig')) # found 'iii'
print(match(r'igs', 'piiig')) # Did not find

# Any char but \n
print(match(r'..g', 'piiig')) # found iig

# \d = digit char, \w = word char
print(match(r'\d\d\d', 'p123g')) # found 123
print(match(r'\w\w\w', '@@abcd!!')) # found abc

# Repetition Examples

# i+ = one or more i's, as many as possible.
print(match(r'pi+', "piiig")) # found piii