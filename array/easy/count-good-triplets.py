# Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.
def countGoodTriplets(arr, a, b, c):
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                    count += 1
    return count

# Example usage:
arr = [3, 0, 1, 1, 9, 7]
a = 7
b = 2
c = 3
print(countGoodTriplets(arr, a, b, c))  # Output: 4
# Time: O(n^3) — Three nested loops
# Space: O(1) — No additional space used