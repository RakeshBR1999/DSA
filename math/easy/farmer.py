# A farmer wants to farm their land with the maximum area where good land is present.
# The "land" is represented as a matrix with ls and Os, where ls mean good land and 0s mean bad land. 
# The farmer only want to farm in a square of good land with the maximum area.
# Please help the farmer to find the maximum area of the land they can farm in good land.
def maxAreaOfLand(land):
    if not land:
        return 0
    rows = len(land)
    cols = len(land[0])
    max_area = 0
    dp = [[0] * cols for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            if land[i][j] == '1':
                dp[i][j] = 1
                if i > 0 and j > 0:
                    # top, left, top left
                    dp[i][j] += min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                max_area = max(max_area, dp[i][j])
    
    return max_area ** 2
# Example usage:        
land = [
    ['1', '0', '1', '1'],
    ['1', '1', '1', '0'],
    ['0', '1', '1', '1'],
    ['1', '0', '0', '1']
]
print(maxAreaOfLand(land))  # Output: 4

# Example usage for maximum 5x5 metrix with 3x3 square area:
land = [
    ['1', '1', '1', '1', '0'],
    ['1', '1', '1', '1', '0'],
    ['1', '1', '1', '1', '0'],
    ['0', '0', '0', '0', '0'],
    ['1', '1', '1', '1', '0']
]

print(maxAreaOfLand(land))  # Output: 9
# Time: O(n*m) — Looping through the matrix
# Space: O(n*m) — Using a 2D array for dynamic programming
# Note: The maximum area is the square of the side length, so we return max_area ** 2.