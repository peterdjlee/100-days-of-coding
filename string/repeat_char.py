# "Maximum Substring With Non-Repeating Characters" from SWE Careers
# Given a string, find the length of the longest substring without repeating characters.

# Example 1:
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

def lengthOfLongestSubstring(s: str):
    if len(s) == 1 or len(s) == 0:
        return len(s)
    maxLength = 1
    for i in range(0, len(s) - 1):
        substr = s[i]
        allCharIsUnique = True
        j = i + 1
        while (allCharIsUnique):
            # If next character doesn't exist
            if j != len(s) and substr.count(s[j]) == 0:
                # Append the next character to substr
                substr += s[j]
                if (len(substr) > maxLength): maxLength = len(substr)
                j += 1
            else:
                allCharIsUnique = False
    return maxLength


def lengthOfLongestSubstring(s: str):
    if len(s) == 1 or len(s) == 0:
        return len(s)
    maxLength = 1
    startIndex = 0
    substr = s[0]
    for endIndex in range(len(s)):
        if substr.find(s[endIndex]) == -1:
            substr += s[endIndex]
            maxLength = max(len(substr), maxLength)
        else:
            startIndex +=1
            substr = s[startIndex]
    return maxLength


str = 'dvdfabc'
print(lengthOfLongestSubstring(str))
