# An AVL tree is a self-balancing Binary Search Tree (BST) where:
# A balanced binary tree or height-balanced binary tree is such a tree whose left and 
# right subtrees' heights differ by not more than 1, 
# which means the height difference could be -1, 0, and 1.
#  A balanced binary tree is also known as a height-balanced tree.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.balance = True
        
        def height(node):
            if not node:
                return -1
            
            left = height(node.left)
            right = height(node.right)
            
            if abs(left - right) > 1:
                self.balance = False
            # why 1 + max(left, right)?
            # The height of the current node is 1 plus the maximum height of its left and right subtrees  
            return 1 + max(left, right)
        
        height(root)
        return self.balance

# Time complexity: O(n), where n is the number of nodes in the binary tree.
# Space complexity: O(h), where h is the height of the binary tree.


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

# Create an instance of the Solution class
sol = Solution()

# Check if the tree is balanced
print("Is the tree balanced?", sol.isBalanced(root))


