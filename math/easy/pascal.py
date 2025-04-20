def n_choose_k(n, k):
    dp = [[0] * (k+1) for _ in range(n+1)]
    
    for i in range(n+1):
        for j in range(min(i, k)+1):
            if j == 0 or j == i:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    
    return dp[n][k]
# Example usage:
n = 5
k = 2
print(f"{n} choose {k} is {n_choose_k(n, k)}")  # Output: 10
# Time Complexity: O(n*k) where n is the number of rows and k is the number of columns
# Space Complexity: O(n*k)

# what is pascal triangle
# Pascal's triangle is a triangular array of the binomial coefficients.
# Each number is the sum of the two numbers directly above it.
# The triangle starts with a single 1 at the top, and each subsequent row has one more number than the previous row.
# The first few rows of Pascal's triangle are:
#         1
#       1   1
#     1   2   1
#   1   3   3   1
# 1   4   6   4   1
# The nth row of Pascal's triangle corresponds to the coefficients of the binomial expansion of (a + b)^n.