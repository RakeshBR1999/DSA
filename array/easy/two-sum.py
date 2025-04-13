# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.
from itertools import combinations
def twosum(nums, target):
    for com in combinations(nums, 2):
        if sum(com) == target:
            return com

# Example usage:
nums = [2,7,11,15]
target = 9
print(twosum(nums, target)) # Output: (2, 7)
nums = [3,2,4]
target = 6
print(twosum(nums, target)) # Output: (2, 4)

# Time: O(n^2) — Looping over all combinations of two numbers
# Space: O(1) — No additional space used

# second method

def twosumm(nums, target):
    num_dict = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in num_dict:
            return (num_dict[complement], i)
        num_dict[nums[i]] = i
# Time: O(n) — Looping over all elements
# Space: O(n) — Dictionary to store indices

nums = [3,2,4]
target = 6
print(twosumm(nums, target))