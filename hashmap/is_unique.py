# Problem for Cracking the Coding Interview: Chapter 1
# 1.1
# Is Unique: Implement an algorithm to determine if a string has all unique characters. 
# What if you cannot use additional data structures?

def isUnique(s):
    dic = {}
    for char in s:
        if char in dic:
            return False
        dic[char] = True
    return True

s = 'hello world'
print(s + ' is unique = ' + str(isUnique(s)))
s = 'abcdefg'
print(s + ' is unique = ' + str(isUnique(s)))
s = 'HELlO'
print(s + ' is unique = ' + str(isUnique(s)))


## Thoughts
# With the no data structure restriction, a brute force solution would be to loop through the string, 
# comparing each character with all the other characters. Doing so would be O(n^2).

# This is very similar to twoSum.py where I can use a hashmap, resulting an O(n) algorithm.

## Solution from the book and what I missed
# First off I could have confirmed what type of string it would be: ASCII vs unicode. 
# If it was unicode I would need more space vs ASCII, which I failed to consider for the problem.

# Knowing the basic ASCII set contains 128 charactes, I could have checked if the len(s) > 128 to 
# immediately return false.

# The book uses bool array[128], which makes me realize how using an array 
# and hashmap can be interchangeable in cases like this

# Either way, I think I understood the core solution. Yay!!