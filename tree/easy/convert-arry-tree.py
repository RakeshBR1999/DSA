# Given an integer array nums where the elements are sorted in ascending order,
#  convert it to a height-balanced binary search tree.
def sortedArrayToBST(nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    if not nums:
        return None
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid + 1:])
    return root

# Time complexity: O(n), where n is the number of elements in the input array.
# Space complexity: O(h), where h is the height of the binary tree.
# The space complexity is O(h) because of the recursion stack, where h is the height of the tree.
# Define TreeNode class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Example usage 
nums = [-10, -3, 0, 5, 9]
root = sortedArrayToBST(nums)

while root:
    print(root.val, end=" -> ")
    root = root.left
