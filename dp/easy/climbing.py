# Climbing Stairs

# The problem is to find the number of distinct ways to reach the nth step, where you can either take 1 or 2 steps at a time.
# The solution can be derived from the Fibonacci sequence, where:
# - The number of ways to reach step n is the sum of the number of ways to reach step n-1 and step n-2.
def climbing_stairs(n: int) -> int:
    if n <= 2:
        return n
    first, second = 1, 2
    for _ in range(3, n + 1):
        first, second = second, first + second
    return second
# Example usage:    
n = 5
print(climbing_stairs(15))  # Output: 8

# Time: O(n) — Looping from 3 to n
# Space: O(1) — Constant space for variables