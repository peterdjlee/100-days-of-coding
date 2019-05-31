# Problem for Cracking the Coding Interview: Chapter 1
# 1.3
# URLify: Write a method to replace all spaces in a string with '%20'. 
# You may assume that the string has sufficient space at the end to hold 
# the additional characters, and that you are given the "true" length of the string.

# EXAMPLE
# Input: "Mr John Smith    ", 13
# Output: "Mr%20John%20Smith"

# Solution 1
# def urlify(s, length):
#     new = ''
#     for i in range(length):
#         if s[i] != ' ':
#             new += s[i]
#         else:
#             new += '%20'
#     return new

# Solution 2
def urlify(s, length):
    # Loop through,
    # If space found, push back the remaining characters 2 spaces back
    # Fill the 3 spaces with '%20'
    for i in range(length):
        if s[i] == ' ':
            for j in range(length - 1, i, -1):
                s[j+2] = s[j]
            s[i] = '%'
            s[i+1] = '2'
            s[i+2] = '0'


s = 'Mr John Smith    '
print(s)
print(s + ' -> urlify! -> ' + urlify(s, 13))




# THOUGHTS / QUESTIONS
# I can't think of any clarifying questions
# Loop through the first {length} characters in the original string to construct a new string 

# I misunderstood the problem and didn't realize I could not make a new string (Solution 1)
# Instead, I should manipulate the original string

# First question, why am I given the length? How can I use the length to solve the problem?
# So that I know where the actual string ends and is not supposed to include spaces.
# This tells me that I probably should be looping through the characters {length} times.

# A problem I ran into: strings in python are immutable.

