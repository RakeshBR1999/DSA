# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
# and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
def merge(nums1, m, nums2, n):
    # Pointer for the last position of nums1
    last = m + n - 1
    
    # Merge in reverse order
    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[last] = nums1[m - 1]
            m -= 1
        else:
            nums1[last] = nums2[n - 1]
            n -= 1
        last -= 1
    
    # If there are remaining elements in nums2, copy them
    while n > 0:
        nums1[last] = nums2[n - 1]
        n -= 1
        last -= 1

# Example usage
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)  # Output: [1, 2, 2, 3, 5, 6]

# Time Complexity: O(m + n)
# The time complexity is O(m + n) because we are merging two sorted arrays.
# Space Complexity: O(1)
# The space complexity is O(1) because we are modifying nums1 in place without using additional space.