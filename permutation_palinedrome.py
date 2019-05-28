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
    permutated = generatePermutation(sLower)
    for perm in permutated:
    return True

def generatePermutation(s):
    permutated = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            permutated.append(s[i:j])
    return permutated

def isPalinedrome(s):
    for i in len(s):
        if s[i] != s[i - 1]:
            return False
    return True

s = 'Tact Coa'
print(s + " is a permutation of a palinedrome = " + str(isPermutationPalinedrome(s)))

s = 'abcd'
print(generatePermutation(s))

# Thoughts
# Question: Is an emptry string a palinedrome? What if it's just 1 character?
#   Assume yes for both
# Therefore if s = '' or s contains 1 character, return True immediately

# Need to try all permutations of the given string and check if the generated string is a palinedrome
# First remove all spaces in the string and either make all chars lower or upper
