# Definition of an N-ary tree node
class Node:
    def __init__(self, val):
        self.val = val
        self.children = []

# Sample Tree:
#         A
#      /  |  \
#     B   C   D
#        / \
#       E   F

# Create nodes
root = Node("A")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")
nodeE = Node("E")
nodeF = Node("F")

# Build the tree
root.children = [nodeB, nodeC, nodeD]
nodeC.children = [nodeE, nodeF]

# Traversal (DFS)
def dfs(node):
    if not node:
        return
    print(node.val)
    for child in node.children:
        dfs(child)

dfs(root)

# Time Complexity: O(N), where N is the number of nodes in the tree
# Space Complexity: O(H), where H is the height of the tree (for recursion stack)
