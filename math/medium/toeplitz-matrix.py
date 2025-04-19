# Toeplitz Matrix
# A Toeplitz matrix is a matrix in which each descending diagonal from left to right is constant.
# Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

# explain to solve the problem
# To determine if a matrix is Toeplitz, we need to check that all elements in each diagonal are the same.
# We can achieve this by iterating through the matrix and checking each diagonal starting from the first row and the first column.
# We can do this by:
# 1. Iterate through each element in the first row and check the diagonal starting from that element.
def isToeplitzMatrix(matrix):
    if not matrix:
        return True

    rows, cols = len(matrix), len(matrix[0])

    # Check diagonals starting from the first row
    for col in range(cols):
        value = matrix[0][col]
        row, c = 0, col
        while row < rows and c < cols:
            if matrix[row][c] != value:
                return False
            row += 1
            c += 1

    # Check diagonals starting from the first column
    for row in range(1, rows):
        value = matrix[row][0]
        r, col = row, 0
        while r < rows and col < cols:
            if matrix[r][col] != value:
                return False
            r += 1
            col += 1

    return True

# Time Complexity: O(m * n) — We check each element in the matrix once.
# Space Complexity: O(1) — We only use a few variables for tracking indices and values.