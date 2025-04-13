# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.
def singleNumber(nums):
    # Initialize a variable to store the result
    result = 0
    # Iterate through each number in the array
    for num in nums:
        # Use XOR operation to find the unique number
        result ^= num 
        # XOR operation works because:
        # 0 0 = 0
        # 0 1 = 1
        # 1 0 = 1
        # 1 1 = 0
        # result = 0 ^ 4 = 4
        # result = 4 ^ 1 = 5
        # result = 5 ^ 2 = 7
        # result = 7 ^ 1 = 6
        # result = 6 ^ 2 = 4
    # Return the unique number
    return result
# Example usage:        
nums = [2, 2, 1]
print(singleNumber(nums))  # Output: 1
nums = [4, 1, 2, 1, 2]
print(singleNumber(nums))  # Output: 4
# Time: O(n) — Looping over the array
# Space: O(1) — Constant space for the result variable

# second method
def single(nums):
    # Create an empty dictionary to store counts
    counts = {}
    # Iterate through each number in the array
    for num in nums:
        # Increment the count for the current number
        counts[num] = counts.get(num, 0) + 1
    # Iterate through the dictionary to find the number with count 1
    for num, count in counts.items():
        if count == 1:
            return num
    return None
# Example usage:
nums = [2, 2, 1]
print(single(nums))  # Output: 1
nums = [4, 1, 2, 1, 2]
print(single(nums))  # Output: 4
# Time: O(n) — Looping over the array
# Space: O(n) — Dictionary to store counts