'''
Regular expressions are a powerful language for matching text patterns. This page gives a basic introduction to regular expressions themselves sufficient for our Python exercises and shows how regular expressions work in Python. The Python "re" module provides regular expression support.
'''

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

## Finds the first/leftmost solution, and within it drives the +
## as far as possible (aka 'leftmost and largest').
## In this example, note that it does not get to the second set of i's.
print(match(r'i+', 'piigiiiii')) # ii

## \s* = zero or more whitespace chars
## Here look for 3 digits, possibly separated by whitespace.
print(match(r'\d\s*\d\s*\d', 'xx1 2   3xx')) # 1 2   3
print(match(r'\d\s*\d\s*\d', 'xx12   3xx')) # 12   3
print(match(r'\d\s*\d\s*\d', 'xx123xx')) # 123

## ^ = matches the start of string, so this fails:
print(match(r'^b\w+', 'foobar')) # Did not find :(

## but without the ^ it succeeds:
print(match(r'b\w+', 'foobar')) # bar

# Email Example
str = "purple alice-b@google.com monkey dishwasher"
print(match(r'\w+@\w+', str)) # b@google

# Square brackets
str = "purple alice-b@google.com monkey dishwasher"
print(match(r'[\w.-]+@[\w.-]+', str)) # alice-b@google.com

# Group Extraction
str = "purple alice-b@google.com monkey dishwasher"
match = re.search(r'([\w.-]+)@([\w.-]+)', str)
if match:
  print(match.group()) # alice-b@google.com (the whole match)
  print(match.group(1)) # alice-b (the username, group 1)
  print(match.group(2)) # google.com (the host, group 2)

# findall
'''
findall() is probably the single most powerful function in the re module. Above we used re.search() to find the first match for a pattern. findall() finds *all* the matches and returns them as a list of strings, with each string representing one match.
'''

# Suppose we have a text with many email addresses
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'

# Here re.findall() returns a list of all the found mail strings
emails = re.findall(r'[\w\.-]+@[\w\.-]+', str)
for email in emails:
  # do something with each found email string
  print(email) # alice@google.com bob@abc.com

# findall and groups
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
tuples = re.findall(r'([\w\.-]+)@([\w\.-]+)', str)
print(tuples)
for tuple in tuples:
  print(tuple[0]) # username (alice, bob)
  print(tuple[1]) # host (google.com, abc.com)