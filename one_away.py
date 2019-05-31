# Problem for Cracking the Coding Interview: Chapter 1
# 1.5
# One Away:
# There are three types of edits that can be performed on strings: 
# insert a character, remove a character, or replace a character.
# Given two strings, write a function to check if they are 0/1 edit away.

# EXAMPLE:
# pale, ple -> True
# pales, pale -> True
# pale, bale -> True
# pale, bae -> False

def isOneAway(s1, s2):
    lenDiff = len(s1) - len(s2)

    if abs(lenDiff) > 1:
        return False

    if len(s1) < len(s2):
        s3 = s1
        s1 = s2
        s2 = s3

    smaller = len(s2)

    diff = 0
    i = 0
    if abs(lenDiff) == 0:
        while diff < 2 and i < smaller:
            if s1[i] != s2[i]:
                diff += 1
            i += 1
    else:
        j = 0
        while diff < 2 and i < smaller:
            if s1[i] != s2[j]:
                diff += 1
                i += 1
            else:
                i += 1
                j += 1
        
    return diff < 2

s1 = 'pale'
s2 = 'ple'
print('"' + s1 + '" and "' + s2 + '" is zero or one edit away = ' + str(isOneAway(s1,s2)))

s1 = 'pales'
s2 = 'pale'
print('"' + s1 + '" and "' + s2 + '" is zero or one edit away = ' + str(isOneAway(s1,s2)))

s1 = 'spale'
s2 = 'pale'
print('"' + s1 + '" and "' + s2 + '" is zero or one edit away = ' + str(isOneAway(s1,s2)))

s1 = 'pale'
s2 = 'bale'
print('"' + s1 + '" and "' + s2 + '" is zero or one edit away = ' + str(isOneAway(s1,s2)))

s1 = 'pale'
s2 = 'bae'
print('"' + s1 + '" and "' + s2 + '" is zero or one edit away = ' + str(isOneAway(s1,s2)))

s1 = 'pale'
s2 = 'ba'
print('"' + s1 + '" and "' + s2 + '" is zero or one edit away = ' + str(isOneAway(s1,s2)))

## Thoughts
# Is there any data structure that I can use?
# I don't think a hashmap would make sense because order of characters matters in this case

# First off if the strings have a length difference > 1, immediately return False
# Two cases: 
#   1. length diff = 0
#   just one letter is different
#   2. length diff = 1 where len(s1) > len(s2)
#   middle or the first char is different:
#       when difference is encountered, 
#       diff++ and compare the next char of s1 with same char of s2
#   last char is different:
#       the while loop will end and knowing there is a difference of 1,
#       the strings must be 1 edit away!

# O(n)