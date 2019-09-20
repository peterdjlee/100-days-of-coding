# Leetcode: 938. Range Sum of BST [Easy]
# Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).
# The binary search tree is guaranteed to have unique values.

# Example 1:
# Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
# Output: 32

# Example 2:
# Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
# Output: 23

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
    # Base case
    if root is None:
        return 0
    # If current node is below range, return sum of left children
    if root.val < L:
        return rangeSumBST(root.right, L, R)
    # If current node is above range, return sum of right children
    if root.val > R:
        return rangeSumBST(root.left, L, R)
    # Current node is in range, return summ of all children
    return root.val + rangeSumBST(root.left, L, R) + rangeSumBST(root.right, L, R)
    
    
