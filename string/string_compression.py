# Problem for Cracking the Coding Interview: Chapter 1
# 1.6
# String Compression:
# Implement a method to perform basic string compression using the counts of repeated characters.
# For example, the string aabcccccaaa would become a2b1c5a3. 
# If the "compressed" string would not become smaller than the original string,
# your method should return the original string. 
# You can assume the string has only uppercase and lowercase letters.

def compressString(s):
    compressed = ''
    count = 0
    prevChar = s[0]
    for char in s:
        if char == prevChar:
            count += 1
        else:
            compressed += prevChar + str(count)
            count = 1
        prevChar = char
    if count != 0:
        compressed += s[len(s) - 1] + str(count)

    if len(compressed) <= len(s):
        return compressed
    else:
        return s

s = 'aabcccccaaa'
print(s + ' = ' + compressString(s))

s = 'abcde'
print(s + ' = ' + compressString(s))

s = 'aaa'
print(s + ' = ' + compressString(s))


## Thoughts
# Thought about using a hashmap/array to map characters and the order but won't work
# because the same letter can appear again

# For loop through the string
# If the character is the same from the previous iteration
#       add count
# else
#       compressed += prevChar + str(count)
#       count = 0
# 


