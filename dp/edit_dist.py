def edit_dist(str1, str2, m, n):
    # If either strings are empty, 
    # addition of length of the other string is the edit distance.
    if m == 0:
        return n
    if n == 0:
        return m

    # If both characters are the same,
    # 0 edit distance for now and compute rest of the string
    if str1[m-1] == str2[n-1]:
        return edit_dist(str1, str2, m-1, n-1)
    
    # Check different cases:
    # 1. If str1 has an extra character
    # 2. If str2 has an extra character
    # 3. If neither has an extra character, 
    # which means a character can be replaced with another.
    return 1 + min(
        edit_dist(str1, str2, m-1, n),
        edit_dist(str1, str2, m, n-1),
        edit_dist(str1, str2, m-1, n-1))

str1 = "sundays"
str2 = "lastmonday"
print(edit_dist(str1, str2, len(str1), len(str2)))