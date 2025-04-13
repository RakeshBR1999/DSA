# Given an integer array nums, move all 0's to the end of it while maintaining the'
# ' relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.
def movezeros(nums):
    left = 0
    right = 0
    while right < len(nums):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        right += 1
    return nums
# Example usage:
nums = [0,1,0,3,12]
print(movezeros(nums)) # Output: [1,3,12,0,0]
nums = [0]
print(movezeros(nums)) # Output: [0]

# Time: O(n) — Looping over all elements
# Space: O(1) — In-place swap

# second method
def move(nums):
    for i in nums:
        if i == 0:
            nums.remove(i)
            nums.append(0)
    return nums