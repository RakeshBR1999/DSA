# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

def symmetric(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if not root:
        return True
    
    def isMirror(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return (t1.val == t2.val) and isMirror(t1.right, t2.left) and isMirror(t1.left, t2.right)
    
    return isMirror(root.left, root.right)

# Time complexity: O(n), where n is the number of nodes in the binary tree.
# Space complexity: O(h), where h is the height of the binary tree.
# can we use the 


# Example usage
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# Creating a symmetric binary tree  
root = TreeNode(1)
root.left = TreeNode(2) 
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

symmetric_result = symmetric(root)
# Printing the original binary tree
print("The binary tree is symmetric." if symmetric_result else "The binary tree is not symmetric.")
