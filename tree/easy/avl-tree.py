# An AVL Tree is a self-balancing Binary Search Tree (BST) where the balance factor of every node
# is between -1 and 1.

# Case | When it Happens | Fix with
# LL (Left-Left) | Insertion in left of left child | Right Rotation
# RR (Right-Right) | Insertion in right of right child | Left Rotation
# LR (Left-Right) | Insertion in right of left child | Left Rotation on left, then Right Rotation
# RL (Right-Left) | Insertion in left of right child | Right Rotation on right, then Left Rotation

# Insert / Delete / Search: O(log n)
# Why? Because the tree stays balanced.


# Common Interview Questions
# Implement AVL Tree insertion (with rotations)

# Rebalance an unbalanced tree

# Find height or balance factor of nodes

# Compare AVL vs BST vs Red-Black Tree

# Validate if a given tree is an AVL tree