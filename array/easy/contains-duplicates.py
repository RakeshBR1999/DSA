# Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.
def conatinesduplicate(nums):
    # Create an empty set to store unique elements
    seen = set() 
    # Iterate through each number in the array
    for num in nums:
        # If the number is already in the set, return True (duplicate found)
        if num in seen:
            return True
        # Otherwise, add the number to the set
        seen.add(num)
    # If no duplicates were found, return False
    return False

# second method
def duplicate(nums):
    d = {}
    for i in nums:
        d[i] = d.get(i, 0) + 1
    for i, k in d.items():
        if k>1:
            return True
    return False
# Example usage:
nums = [1, 2, 3, 4, 5]
print(conatinesduplicate(nums))  # Output: False
nums = [1, 2, 3, 4, 5, 1]
print(conatinesduplicate(nums))  # Output: True

# Time: O(n) — Looping over the array
# Space: O(n) — Set to store unique elements