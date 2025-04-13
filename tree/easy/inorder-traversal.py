

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)
        
        inorder(root)
        return res

# Create a binary tree manually for testing
# For example:
#        1
#       / \
#      2   3
#     / \
#    4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Instantiate the Solution class
sol = Solution()

# Call the inorderTraversal method
result = sol.inorderTraversal(root)

# Print the result
print(result)  # Output should be [4, 2, 5, 1, 3]

# In-order: Visits left child, root, right child. Used for printing sorted elements in a binary search tree.
# Pre-order: Visits root, left child, right child. Useful for copying or cloning a tree.
# Post-order: Visits left child, right child, root. Used for deleting tree nodes or freeing memory.
