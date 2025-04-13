#  Remove Duplicates from Sorted Array

# Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
def removeduplicate(nums):
    if not nums:
        return 0
    # Initialize the index for the next unique element
    unique_index = 1
    # Iterate through the array starting from the second element
    for i in range(1, len(nums)):
        # If the current element is different from the previous one
        if nums[i] != nums[i - 1]:
            # Assign it to the unique index and increment the index
            nums[unique_index] = nums[i]
            unique_index += 1
    # Return the length of the array with unique elements
    return unique_index
# Example usage:        
nums = [1, 1, 2, 2, 3]
length = removeduplicate(nums)
print(length)  # Output: 3

# Time: O(n) — Looping over the array       
# Space: O(1) — In-place modification
    
def remo(nums):
    d = []
    for i in nums:
        if i not in d:
            d.append(i)
    return d

# Example usage:        
nums = [1, 1, 2, 2, 3]
length = remo(nums)
print(length)  # Output: [1, 2, 3]

    