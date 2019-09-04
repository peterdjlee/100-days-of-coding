# "Flipping an Image" from Leetcode

# Given a binary matrix A, we want to flip the image horizontally, 
# then invert it, and return the resulting image.

# To flip an image horizontally means that each row of the image is reversed.  
# For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. 
# For example, inverting [0, 1, 1] results in [1, 0, 0].

# EXAMPLE 1
# Input: [[1,1,0],[1,0,1],[0,0,0]]
# Output: [[1,0,0],[0,1,0],[1,1,1]]
# Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
# Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]

# EXAMPLE 2
# Input: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
# Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
# Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]

# Notes:
# 1 <= A.length = A[0].length <= 20
# 0 <= A[i][j] <= 1

def flipAndInvertImage(matrix):
    height = len(matrix)
    width = len(matrix[0])
    for r in range(height):
        for c in range(width):
            if c < int(width / 2):
                # Invert
                matrix[r][c] = 0 if matrix[r][c] == 1 else 1

                # Swap
                temp = matrix[r][width - 1 - c]
                matrix[r][width - 1 - c] = matrix[r][c]
                matrix[r][c] = temp

                # Invert
                matrix[r][c] = 0 if matrix[r][c] == 1 else 1
        if width % 2 == 1: # If the width is odd
            # Invert middle
            matrix[r][int(width / 2)] = 0 if matrix[r][int(width / 2)] == 1 else 1
    return matrix

mat = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
solution = [[1,0,0],[0,1,0],[1,1,1]]
# print(mat)
if flipAndInvertImage(mat) == solution:
    print("Case 1 Passed")
else:
    print("Case 1 Failed")

mat = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]
solution = [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
if flipAndInvertImage(mat) == solution:
    print("Case 2 Passed")
else:
    print("Case 2 Failed")
