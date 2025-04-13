def knapsack(weights, values, W):
    n = len(weights)
    # Why (n+1) and (W+1)? To include the base case of 0 items or 0 capacity.
    dp = [[0]*(W+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for w in range(1, W+1):
            if weights[i-1] <= w:
                # Add the items value, and check the best value for remaining capacity
                dp[i][w] = max(dp[i-1][w], values[i-1] + dp[i-1][w - weights[i-1]])
            else:
                dp[i][w] = dp[i-1][w]
    print("DP Table:")
    for row in dp:
        print(row)
    return dp[n][W]


W = 4
weights = [3, 4, 5]
values =  [30, 50, 60]

print(knapsack(weights, values, W))

# Time: O(n * W) — Looping over all items and capacities

# Space: O(n * W) — 2D table

# 1d DP approach
def knapsack(weights, values, W):
    n = len(weights)
    dp = [0] * (W + 1)

    for i in range(n):
        for w in range(W, weights[i] - 1, -1):
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]])

    return dp[W]

# Time: O(n * W) — Looping over all items and capacities

# Space: O(W) — 2D table