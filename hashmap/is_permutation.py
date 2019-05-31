# Problem for Cracking the Coding Interview: Chapter 1
# 1.2
# Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.


def isPermutation(s1, s2):
    if len(s1) != len(s2):
        return False
    dic = {}
    for char in s1:
        dic[char] = True
    for char in s2:
        if char not in dic:
            return False
    return True

s1 = 'hello world'
s2 = 'world hello'
print('"'+ s1 + '" is a permutation of "' + s2 + '" = ' + str(isPermutation(s1, s2)))

s1 = 'oo o'
s2 = 'ooo o'
print('"'+ s1 + '" is a permutation of "' + s2 + '" = ' + str(isPermutation(s1, s2)))

s1 = 'abc'
s2 = 'cba'
print('"'+ s1 + '" is a permutation of "' + s2 + '" = ' + str(isPermutation(s1, s2)))

## Thoughts
# I first need to think about what defines a permutation.
# I would define a permutation to be when two string contain the same characters independent of order.
# I think I can use a hashmap to keep track of which characters I have, 
# and when I add the second string, if any character doesn't exist, then return false.

## Solution from the book and what I missed
# Again I failed to ask clarifying questions about the parameter. 
# Does captalization matter?
# Do white-spaces matter?

# A solution from the book that I did not think of is to sort the two strings then 
# see if they are equal.

# The book again used an array instead of hash map. 
# Not sure if there is a reason not to use a hash map in this case.
