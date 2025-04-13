from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(root, min_val, max_val):
            if not root:
                return True
            if root.val <= min_val or root.val >= max_val:
                return False
# isValid(root.left, min_val, root.val): This recursively checks if the left subtree of the current node (root) is a valid BST. 
# We pass min_val as the minimum allowed value for nodes in the left subtree and root.val as the maximum allowed value.
#  This ensures that all nodes in the left subtree are less than the current node's value (root.val).

# isValid(root.right, root.val, max_val): Similarly, this recursively checks if the right subtree of the current node (root)
#  is a valid BST. We pass root.val as the minimum allowed value for nodes in the right subtree and max_val as the maximum allowed value. 
# This ensures that all nodes in the right subtree are greater than the current node's value (root.val).
            return isValid(root.left, min_val, root.val) and isValid(root.right, root.val, max_val)

# float("-inf"): This represents the smallest possible floating-point value, which is considered as negative infinity. 
# float("inf"): This represents the largest possible floating-point value, which is considered as positive infinity.
        return isValid(root, float("-inf"), float("inf"))

# Time complexity: O(n), where n is the number of nodes in the binary tree. 
# Space complexity: O(h), where h is the height of the binary tree due to the recursion stack.

# Create a binary tree manually for testing
root = TreeNode(2)
root.left = TreeNode(1)
# root.left = TreeNode(4)
root.right = TreeNode(3)

# Instantiate the Solution class
sol = Solution()

# Call the isValidBST method
result = sol.isValidBST(root)

# Print the result
print(result)  # Output should be True

