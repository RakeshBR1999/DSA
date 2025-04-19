# You are a professional robber planning to rob houses along a street. 
# Each house has a certain amount of money stashed, the only constraint stopping you from 
# robbing each of them is that adjacent houses have security systems connected and 
# it will automatically contact the police if two adjacent houses were broken into on the same night.

# explain thsi problem
# Given an integer array nums representing the amount of money of each house,
# return the maximum amount of money you can rob tonight without alerting the police.
# The problem can be solved using dynamic programming.
# The idea is to maintain a running total of the maximum amount of money that can be robbed
# at each house, taking into account the constraint that adjacent houses cannot be robbed.
# The dynamic programming approach involves iterating through the array of houses and
# calculating the maximum amount of money that can be robbed up to each house.
# The recurrence relation is as follows:
# dp[i] = max(dp[i-1], dp[i-2] + nums[i])
# where dp[i] is the maximum amount of money that can be robbed up to house i.
# The first term dp[i-1] represents the case where the current house is not robbed,
# and the second term dp[i-2] + nums[i] represents the case where the current house is robbed.
# The base cases are:
# dp[0] = nums[0] (if there is at least one house)
# dp[1] = max(nums[0], nums[1]) (if there are at least two houses)
# The final answer will be stored in dp[n-1], where n is the number of houses.
# The time complexity of this approach is O(n), where n is the number of houses,
# and the space complexity is O(n) for the dp array.
def rob(nums):
    if not nums:
        return 0
    n = len(nums)
    if n == 1:
        return nums[0]
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    return dp[-1]
# Example usage:
nums = [2, 7, 9, 3, 1]
print(rob(nums))  # Output: 12

# Time: O(n) — Looping through the array
# Space: O(n) — Array to store maximum amounts
# Optimized Space Complexity
