# Problem from Cracking the Coding Interview: Chapter 1
# 1.9: String Rotation
# Assume you have a method isSubstring which checks if one word is a substring of another.
# Given two strings, s1 and s2, write code to check if s2 is a rotation of s1
# using only one call to isSubstring 
# (e.g. "waterbottle" is a rotation of "erbottlewat")

def isSubstring(s1, s2):
    if s2 in s1:
        return True
    if s1 in s2:
        return True

s1 = 'water'
s2 = 'waterbottle'


def isRotation(s1, s2):
    if len(s1) != len(s2):
        return False
    

## Thoughts
# What does it really mean for a string to be "in rotation"?
# The two strings are in same order, but not in the same place (since order is invovled, can't hash)
# A brute force solution would be to