# Given an integer array nums, find the subarray with the largest sum, and return its sum.
def maxSubArray(nums):
    max_sum = nums[0]
    current_sum = nums[0]
    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
    return max_sum
# Example usage:        
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))  # Output: 6

# Time: O(n) — Looping through the array
# Space: O(1) — No additional space used