# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree 
# and inorder is the inorder traversal of the same tree, construct and return the binary tree.
def binaryTree(preorder, inorder):
    if not preorder or not inorder:
        return None

    root_val = preorder[0]
    root = TreeNode(root_val)

    # Find the index of the root in inorder array
    root_index = inorder.index(root_val)

    # Recursively construct the left and right subtrees
    # why inorder[:root_index] and inorder[root_index + 1:]?
    # The left subtree will be in the range of inorder[:root_index]
    root.left = binaryTree(preorder[1:root_index + 1], inorder[:root_index])
    root.right = binaryTree(preorder[root_index + 1:], inorder[root_index + 1:])

    return root
# why O(n^2)?
# The time complexity is O(n^2) because the index() method is called for each node in the preorder array.
# The index() method has a time complexity of O(n) in the worst case,


# Time complexity: O(n^2), where n is the number of nodes in the tree.
# Space complexity: O(h), where h is the height of the tree.
# The space complexity is O(h) because of the recursion stack, where h is the height of the tree.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Example usage:
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
root = binaryTree(preorder, inorder)


# Function to print the tree in inorder
def print_inorder(node):
    if node:
        print_inorder(node.left)
        print(node.val, end=' ')
        print_inorder(node.right)
print_inorder(root)