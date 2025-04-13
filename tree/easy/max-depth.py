# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the 
# longest path from the root node down to the farthest leaf node.

def maxDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root is None:
        return 0
    lt = maxDepth(root.left)
    rt = maxDepth(root.right)
    return max(lt, rt) + 1




# Example usage
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Creating a binary tree
root = TreeNode(1)      
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.left.left.left = TreeNode(8)
root.left.left.right = TreeNode(9)
root.right.left.left = TreeNode(10)
root.right.left.right = TreeNode(11)
# Printing the original binary tree
current = root
while current:
    print(current.val, end=" -> ")
    current = current.left
print()
# Finding the maximum depth of the binary tree
result = maxDepth(root)
print("Maximum depth of the binary tree:", result)

# Time complexity: O(n), where n is the number of nodes in the binary tree.
# Space complexity: O(h), where h is the height of the binary tree.