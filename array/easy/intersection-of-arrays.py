# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must appear as many times as it shows in both arrays and
# you may return the result in any order.
def intersect(nums1,nums2):
    l = []
    for i in nums1:
        if i in nums2:
            l.append(i)
            nums2.remove(i)
    return l
# Example usage:    
nums1 = [1,2,2,1]
nums2 = [2]
print(intersect(nums1, nums2)) # Output: [2]
nums1 = [1,2,2,1]
nums2 = [2,2]
print(intersect(nums1, nums2)) # Output: [2, 2]
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(intersect(nums1, nums2)) # Output: [9, 4]

# Time: O(n) — Looping over all elements in nums1
# Space: O(n) — List to store the intersection

# second approach
def intersect(nums1, nums2):
    count = {}
    result = []
    
    # Count occurrences of each number in nums1
    for num in nums1:
        count[num] = count.get(num, 0) + 1
    
    # Find intersection with nums2
    for num in nums2:
        if num in count and count[num] > 0:
            result.append(num)
            count[num] -= 1
    
    return result
# Example usage:
nums1 = [1,2,2,1]
nums2 = [2]
# Time: O(n) — Looping over all elements in nums1 and nums2
# Space: O(n) — Dictionary to store counts