from typing import Optional, List

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        self.helper(root, res, 0)
        return res
    
    def helper(self, root, res, height):
        if not root:
            return 
        if height >= len(res):
            res.append([])
        res[height].append(root.val)
        self.helper(root.left, res, height+1)
        self.helper(root.right, res, height+1)



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

sol = Solution()
result = sol.levelOrder(root)
print(result)

# Time complexity: O(n), where n is the number of nodes in the binary tree.
# Space complexity: O(n), where n is the number of nodes in the binary tree.
