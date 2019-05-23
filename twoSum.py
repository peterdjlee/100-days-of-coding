# Two Sum Problem from LeetCode 
# Given an array of integers, return indices of the two numbers such that they add 
# up to a specific target.

# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

nums = [2, 4, 6, 7, 8, 10, 12]
target = 9

# Solution 1
# def twoSum(nums, target):
#     length = len(nums)
#     for i in range(length):
#         for j in range(i + 1, length):
#             if (nums[i] + nums[j] == target):
#                 return [i, j]

# Solution 2 after hint from LeetCode
# def twoSum(nums, target):
#     d = {}
#     # Maps the nums value
#     for i in range(len(nums)):
#         d[nums[i]] = i
    
#     # Looks up the appopriate number to add up to target for each value
#     for x in d:
#         if (target - x) in d and d[x] != d[target - x]:
#             return [d[x], d[target - x]]

# Solution 3 after hint from LeetCode
def twoSum(nums, target):
    d = {}
    for i in range(len(nums)):
        if (target - nums[i]) in d:
            print(d)
            return [i, d[target - nums[i]]]
        d[nums[i]] = i

print(twoSum(nums, target))

# THOUGHTS
# Solution 1:
#   Running a loop from through the list to compare each value's sum with another.
#   O(n^2) 
#       n - 1 + n - 2 + ... + 1 where the sum is n(n + 1)/2 = n^2 without constants and non-dominant terms

# Solution 2:
#   By using a hashmap, the lookup time for the value needed is O(1); 
#       There is no more a 2nd loop looking through.
#   O(n)

# Solution 3:
#   Optimizes solution 2 further by looking for the complement value as the numbers are added to the dict;
#       No need to add unnecessary values to the dictionary.
#   Still O(n)

