# Problem for Cracking the Coding Interview: Chapter 1
# 1.4
# Palinedrone Permutation: 
# Given a string, write a function to check if it is a permutation of a palindrome. 
# A palindrome is a word or phrase that is the same forwards and backwards. 
# A permutation is a rearrangement of letters.
# The palinedrome does not need to be limited to just dictionary words. You can ignore casting and non-letter characters.
# EXAMPLE:
# Input: Tact Coa
# Output: True (permutations: "taco cat", "atco cta", etc.)

def isPermutationPalinedrome(s):
    if len(s) == 0 or len(s) == 1:
        return True
    sLower = s.lower()
    sLower = sLower.replace(' ', '')
    count = {}

    for char in sLower:
        count[char] = 0 # Initialize the map

    for char in sLower:
        count[char] += 1

    oddChar = 0
    for char in count:
        if count[char] % 2 == 1:
            oddChar += 1
    if oddChar > 1:
        return False
    return True

s = 'Tact Coa'
print(s + " is a permutation of a palinedrome = " + str(isPermutationPalinedrome(s)))

s = 'AABBBCC'
print(s + " is a permutation of a palinedrome = " + str(isPermutationPalinedrome(s)))

s = 'ABBBCC'
print(s + " is a permutation of a palinedrome = " + str(isPermutationPalinedrome(s)))

s = 'ABBCC'
print(s + " is a permutation of a palinedrome = " + str(isPermutationPalinedrome(s)))


# Thoughts
# Question: Is an emptry string a palinedrome? What if it's just 1 character?
#   Assume yes for both
# Therefore if s = '' or s contains 1 character, return True immediately

# Need to try all permutations of the given string and check if the generated string is a palinedrome
# First remove all spaces in the string and either make all chars lower or upper

# It was way too complicated to do the first attempt, so I thought about it differently.
# Since a palinedrome means that it has an even amount of each character and only 1 odd number of character

# O(n)

# An alternate solution can be counting the number of odd characters as they are added
# then check at the end. But this is not necessarily optimzing our original algorithm.
