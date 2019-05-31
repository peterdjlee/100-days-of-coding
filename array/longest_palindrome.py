# Problem found on internet:
# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example:
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer

# Input: "cbbd"
# Output: "bb"


def findPal(s):
  length = len(s)
  for i in range(length):
    if (s[i] != s[length - 1 - i]):
      return False
  return True

s = 'abbba'
print(s + " is a palinedrome = " + str(findPal(s)))

def findPalSubs(s):
  length = len(s)
  listOfPalSubs = []
  for i in range(length):
    for j in range(i + 1, length + 1):
      if findPal(s[i:j]):
        listOfPalSubs.append(s[i:j])
  longestPalSub = ''
  maxLength = 0
  for palSub in listOfPalSubs:
    if len(palSub) > maxLength:
      longestPalSub = palSub
      maxLength = len(palSub)
    
  return longestPalSub
s = 'abba'
print(findPalSubs(s))
s = 'babad'
print(findPalSubs(s))
s = 'cbbd'
print(findPalSubs(s))
s = 'referannaracecar'
print(findPalSubs(s))

      



## Thoughts
# A palinedrom is defined by a string where it reads the same backwards as forwards.
# First, figure out how to find a palinedrome
# Loop through string upto len(s)/2, check the opposite character and see if it matches

# Second, figure out how to get a list of palinedromes in a given string.
# A brute force solution would be to try run a nested loop and pass in s[i:j]
